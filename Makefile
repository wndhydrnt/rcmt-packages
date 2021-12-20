apply:
	@docker run \
	-e "RCMT_GIT_EMAIL=$(RCMT_GIT_EMAIL)" \
	-e "RCMT_GIT_USERNAME=$(RCMT_GIT_USERNAME)" \
	-e "RCMT_GITHUB_ACCESS_TOKEN=$(RCMT_GITHUB_ACCESS_TOKEN)" \
	-e "RCMT_GITHUB_USERNAME=$(RCMT_GITHUB_USERNAME)" \
	--rm \
	-v "$(PWD):/opt/work" \
	--entrypoint=/opt/work/entrypoint.sh \
	wandhydrant/rcmt:main
