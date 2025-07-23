#!/usr/bin/env just --justfile

alias s := sync
alias t := test
alias pc := precommit

set dotenv-load := true

# List available recipes
default:
  @just --list

# Install/sync
sync:
  uv sync --all-packages

# Run tests
test:
  uv run pytest -v

# Run format/lint/check
precommit:
  just sync
  just test
  just clean-nb
  
# Run the PLM model generate example
# download data from: https://dl.fbaipublicfiles.com/plm/dummy_datasets.tar.gz
plm-gen:
  CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES plm-generate --ckpt facebook/Perception-LM-8B \
    --media_type image \
    --media_path apps/plm/dummy_datasets/image/images/14496_0.PNG \
    --question 'Describe the bar plot in the image.'

# Strip outputs from Jupyter notebooks
clean-nb:
  uv run nbstripout nb/*.ipynb

# Remove cached files
clean *args:
  just clean-nb
  uv run pyclean . \
    --debris cache coverage package pytest ruff \
    {{ args }}
  uv cache prune