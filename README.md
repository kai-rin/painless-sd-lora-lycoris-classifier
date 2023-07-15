# Lora Lyco Classifier

[日本語の説明](#lora-lyco-分類器)は英語の後にあります。

Dedicated to all mankind who despair at being told to put LORA and Lycoris files in separate folders.

This is a simple script that identifies whether `.safetensors` files are "LORA" or "LyCORIS" and moves them to the respective directories. It identifies them from the `.civitai.info` file.

This assumes the use of the [Stable-Diffusion-Webui-Civitai-Helper extension](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper).

## How to use

Simply place the `lora_lyco_classifier.py` in a directory containing `.civitai.info` files and other related files (such as `.safetensors` and `.preview.png`).

Run the script using Python 3. No additional arguments are required.

For macOS or Linux:

```Python
python3 lora_lyco_classifier.py
```

On Windows:

```Python
py lora_lyco_classifier.py
```

Or you can directly execute the script:

```cmd
.\lora_lyco_classifier.py
```

After executing the script, files will be moved to the '_lora' and '_lycoris' directories through the following process:

1. It scans all files in the same directory as the script.

2. It identifies whether the 'model type' from the .civitai.info file is either 'LORA' or 'LyCORIS'.

3. It creates '_lora' and '_lycoris' directories.

4. Based on the 'model type', it moves 'LOAR' and 'LyCORIS' files to their respective directories.

# Lora Lyco 分類器

LORAとLyCORISファイルを別々のフォルダで管理しやすくするために作りました。

`.safetensors`ファイルが"LORA"か"LyCORIS"かを判別し各ディレクトリに移動するシンプルなスクリプトです。[Stable-Diffusion-Webui-Civitai-Helper extension](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper) により生成される `.civitai.info` から判別します。

## 使い方

`lora_lyco_classifier.py`を`.civitai.info`ファイルとその他の関連ファイル（`.safetensors`や`.preview.png`）を含むディレクトリに配置してください。

Python 3を使用してスクリプトを実行します。追加の引数は必要ありません

macOS または Linux:

```Python
python3 lora_lyco_classifier.py
```

Windows:

```Python
py lora_lyco_classifier.py
```

またはスクリプトを直接実行:

```cmd
.\lora_lyco_classifier.py
```

スクリプトを実行すると以下の工程を経て'_lora'と'_lycoris'ディレクトリにファイルが移動します。

1. スクリプトと同じディレクトリ内のすべてのファイルをスキャンします。

2. `.civitai.info`ファイルの内容から'model type'が'LORA'または'LyCORIS'のいずれであるか判別します。

3. '_lora' および '_lycoris' ディレクトリを作成します。

4. 'model type'に基づき'LOAR', 'LyCORIS'ファイルをそれぞれのディレクトリに移動します。
