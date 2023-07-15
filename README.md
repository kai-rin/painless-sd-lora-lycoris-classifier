# Lora Lyco Classifier

[日本語の説明](#lora-lyco-分類器)は英語の後にあります。

I've crafted this nifty tool to make your life easier when dealing with LORA and LyCORIS files by managing them in separate folders.

This script is a simple solution that identifies whether `.safetensors` files are of type "LORA" or "LyCORIS", and moves them into respective directories. The determination is made based on the `.civitai.info` files generated by the [Stable-Diffusion-Webui-Civitai-Helper extension](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper).

## How to Use

Place `lora_lyco_classifier.py` in the directory that contains your `.civitai.info` files and any related files (like `.safetensors` and `.preview.png`).

You'll need Python 3 to run the script. No additional arguments are required.

On macOS or Linux:

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

When you run the script, files will be moved to the '_lora' and '_lycoris' directories following these steps:

1. The script scans all the files in the same directory.

2. It determines whether the 'model type' from the .civitai.info files is either 'LORA' or 'LyCORIS'.

3. It creates '_lora' and '_lycoris' directories.

4. Based on the 'model type', it moves 'LORA' and 'LyCORIS' files into their respective directories. Enjoy your newly organized files!

## How to Use (Windows: Run exe file)

I've created an executable file as running the script can be a bit of a hassle.

Place the `lora_lyco_classifier.exe` in the directory that contains the `.civitai.info` file and other related files (such as `.safetensors` and `.preview.png`). Running the file will perform the same actions as described above.

[Releases: lora-lyco-classifier](https://github.com/kai-rin/painless-sd-lora-lycoris-classifier/releases)

# Lora Lyco 分類器

LORAとLyCORISファイルを別々のフォルダで管理しやすくするために作りました。

`.safetensors`ファイルが"LORA"か"LyCORIS"かを判別し各ディレクトリに移動するシンプルなスクリプトです。[Stable-Diffusion-Webui-Civitai-Helper extension](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper) により生成される `.civitai.info` から判別します。

## 使い方（Pythonスクリプト実行）

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

## 使い方（Windows: exeファイル実行）

スクリプトの実行が面倒なので実行ファイルも作りました。

`lora_lyco_classifier.exe`を`.civitai.info`ファイルとその他の関連ファイル（`.safetensors`や`.preview.png`）を含むディレクトリに配置して実行すれば上記と同じ挙動をします。

[Releases: lora-lyco-classifier](https://github.com/kai-rin/painless-sd-lora-lycoris-classifier/releases)
