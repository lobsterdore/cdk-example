FROM ubuntu:bionic

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt update && \
	DEBIAN_FRONTEND=noninteractive apt install --no-install-recommends -yq \
	curl \
	software-properties-common \
	gpg-agent && \
	curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
	DEBIAN_FRONTEND=noninteractive apt install -yq nodejs && \
	npm install -g aws-cdk@1.1.0 && \
	mkdir -p /code && \
	apt clean -y  && \
	apt autoclean -y && \
	rm -rf /var/lib/apt/lists/*
