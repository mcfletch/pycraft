# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

apidoc:

	sphinx-apidoc -o "$(SOURCEDIR)/api" "--force" "--separate" "--no-toc" "$(SOURCEDIR)/../../pycraft"

# TODO: this is actually relying on the introspection having been run
# which may not have happened if you've just checked out the code...
proxydoc:
	pycraft-doc-generator

autodocs: apidoc proxydoc

.PHONY: help Makefile apidoc proxydoc autodocs



# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
