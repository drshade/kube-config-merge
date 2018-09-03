# kube-config-merge.py

## Installation
Requires pyyaml to be installed

    $ pip install pyyaml

Usage:

    $ python kube-config-merge.py <target_config> <source_configs...>

For example:

      $ python kube-config-merge.py ~/.kube/config.vg *-devops/kube-config/config
      $ export KUBECONFIG=~/.kube/config.vg

## Tips for a cool shell experience ##

Install kubectx

    $ brew install kubectx

Provides you with 2 things:
  * kubectx - allows you to list clusters and switch between them easily, only caveat is that it must all be in a single kube-config file (see tool above!)
  * kubens - allows you to list and set a default namespace for a particular cluster (saving you typing v1-svq-qa everytime!)


Install zsh with kubectl & kube-ps1 plugin to change your prompt depending on what cluster/namespace you have selected:
  * Goto https://ohmyz.sh/ and install zsh with oh-my-zsh
  * Edit your ~/.zshrc config and setup kubectl & kube-ps1 - see Tom's example below


### Toms .zshrc snippet for nice kubernetes prompts

    plugins=(
      git
      gitignore
      kubectl
      kube-ps1
      helm
      kops
      iterm2
      docker
      aws
      brew
      npm
      terraform
      shrink-path
    )

    source $ZSH/oh-my-zsh.sh
    source <(kubectl completion zsh)

    # kube-ps1 stuff
    export KUBE_PS1_PREFIX=\[
    export KUBE_PS1_SUFFIX=\]
    export KUBE_PS1_DIVIDER='|'
    export KUBE_PS1_SYMBOL_ENABLE=false

    export PROMPT='%{$fg_bold[white]%}$USER@%M%{$reset_color%}/$(kube_ps1) %{$fg[white]%}$(shrink_path -f)%{$reset_color%} $(git_prompt_info)'
