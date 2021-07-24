apply:
	docker run -e "RCMT_GITHUB_ACCESS_TOKEN=$(RCMT_GITHUB_ACCESS_TOKEN)" --rm -v "$(PWD):/opt/work" wandhydrant/rcmt run --config /opt/work/rcmt.yaml --packages /opt/work/packages /opt/work/matcher.yaml
