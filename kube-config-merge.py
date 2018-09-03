import sys
import yaml
import json

target_file = sys.argv[1]
print "Target %s"%target_file

source_files = sys.argv[2:]

# Could be a yaml or json file
#
def parse_kube_config(filename):
    try:
        print "Reading %s"%filename
        data = open(filename).read()

        # yaml.load seems to tolerate json too!
        config = yaml.load(data)

        return config
    except Exception, e:
        print e.message
        sys.exit -1

parsed = [parse_kube_config(file) for file in source_files]

# Now do an effective flatmap to get it all into a single structure
target_config = {
    "apiVersion": "v1",
    "kind": "Config",
    "current-context": "",
    "clusters": [],
    "contexts": [],
    "users": [],
}

for config in parsed:
    for cluster in config['clusters']:
        print "  Appending cluster: %s"%(cluster["name"])
        target_config['clusters'].append(cluster)
    for context in config['contexts']:
        print "  Appending context: %s"%(context["name"])
        target_config['contexts'].append(context)
    for user in config['users']:
        print "  Appending user: %s"%(user["name"])
        target_config['users'].append(user)

open(target_file, 'w').write(yaml.dump(target_config))

print "Wrote %s"%target_file
