Train VQGAN
```
python main.py --base configs/custom_vqgan.yaml -t True --gpus 0,1
```
Train Transformer
```
python main.py --base configs/custom_transformer.yaml -t True --gpus 0,1
```




Fix this error
```
  File "/home/epinyoan/git/taming-transformers/taming/modules/transformer/mingpt.py", line 17, in <module>
    from transformers import top_k_top_p_filtering
  File "/home/epinyoan/miniconda3/envs/taming/lib/python3.8/site-packages/transformers/__init__.py", line 43, in <module>
    from . import dependency_versions_check
  File "/home/epinyoan/miniconda3/envs/taming/lib/python3.8/site-packages/transformers/dependency_versions_check.py", line 41, in <module>
    require_version_core(deps[pkg])
  File "/home/epinyoan/miniconda3/envs/taming/lib/python3.8/site-packages/transformers/utils/versions.py", line 94, in require_version_core
    return require_version(requirement, hint)
  File "/home/epinyoan/miniconda3/envs/taming/lib/python3.8/site-packages/transformers/utils/versions.py", line 85, in require_version
    if want_ver is not None and not ops[op](version.parse(got_ver), version.parse(want_ver)):
  File "/home/epinyoan/miniconda3/envs/taming/lib/python3.8/site-packages/packaging/version.py", line 52, in parse
    return Version(version)
  File "/home/epinyoan/miniconda3/envs/taming/lib/python3.8/site-packages/packaging/version.py", line 197, in __init__
    raise InvalidVersion(f"Invalid version: '{version}'")
packaging.version.InvalidVersion: Invalid version: '0.10.1,<0.11'
```
by from [here](https://github.com/CompVis/latent-diffusion/issues/207)
```
~/miniconda3/envs/taming/bin/pip install packaging==21.3
~/miniconda3/envs/taming/bin/pip install 'torchmetrics<0.8'
```