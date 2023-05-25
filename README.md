# Lora Lyco Classifier

[日本語の説明](#lora-lyco-分類器)は英語の後にあります。

Dedicated to all mankind who despair at being told to put LORA and Lycoris files in separate folders.

This is a super simple script that determines whether a `.safetensors` file is "LORA" or "LyCORIS" based on `.civitai.info` file information and moves it to the respective directory.

Required: Use of the [Stable-Diffusion-Webui-Civitai-Helper extension](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper).

## How it Works

The script operates as follows:

1. Scans all files in the directory where the script exists.

2. Determines from the contents of the `.civitai.info` file whether the 'model type' is either 'LORA' or 'LyCORIS'.

3. Creates 'LORA' and 'LyCORIS' directories.

4. Moves 'LORA' and 'LyCORIS' files to their respective directories based on 'model type'.

## Usage

Simply place `lora_lyco_classifier.py` in a directory that contains `.civitai.info` files and their associated files (`.safetensors` and `.preview.png`).

Execute the script using Python 3. No additional arguments are required:

On macOS and Linux:

```Python
python3 lora_lyco_classifier.py
```

On Windows:

```Python
py lora_lyco_classifier.py
```

or, you can run the script directly:

```cmd
.\lora_lyco_classifier.py
```

Upon running the script, the files are moved to 'Lora' and 'LyCORIS' directories.

# Lora Lyco 分類器

LORAとLyCORISファイルを別々のフォルダに配置せよと言われ絶望している全人類に捧ぐ。

`.safetensors`ファイルが"LORA"か"LyCORIS"かを判別し各ディレクトリに移動するシンプルなスクリプトです。`.civitai.info`から判別しています。

[Stable-Diffusion-Webui-Civitai-Helper extension](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper) の利用を前提にしています。

## 動作方法

スクリプトは次のように動作します：

1. スクリプトが存在するディレクトリ内のすべてのファイルをスキャンします。

2. `.civitai.info`ファイルの内容から'model type'が'LORA'または'LyCORIS'のいずれであるか判別します。

3. 'LORA' および 'LyCORIS' ディレクトリを作成します。

4. 'model type'に基づき'LOAR', 'LyCORIS'ファイルをそれぞれのディレクトリに移動します。

## 使い方

シンプルに`lora_lyco_classifier.py`を`.civitai.info`ファイルとその他の関連ファイル（`.safetensors`や`.preview.png`）を含むディレクトリに配置してください。

Python 3を使用してスクリプトを実行します。追加の引数は必要ありません：

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

スクリプトを実行すると'Lora'と'LyCORIS'ディレクトリにファイルが移動します。
