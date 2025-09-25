#!/bin/zsh
export GIT_SSH_COMMAND="ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes -o ConnectTimeout=30"
git push -v git@github.com:Darcy-Kevin/UI.git master