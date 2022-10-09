#/bin/bash

export RUNNER_ALLOW_RUNASROOT="1"

wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
sudo ./sam-installation/install

mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.297.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.297.0/actions-runner-linux-x64-2.297.0.tar.gz
tar xzf ./actions-runner-linux-x64-2.297.0.tar.gz
./config.sh --url https://github.com/hxrsmurf/spotify --token [key]--ephemeral
./run.sh &