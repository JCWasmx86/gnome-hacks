format:
	isort gnomehacks/
	black gnomehacks/
	black gnomehacks/
lint:
	pylint gnomehacks/ --ignore-patterns "gnomehacks/migrations/[\S+].py"
