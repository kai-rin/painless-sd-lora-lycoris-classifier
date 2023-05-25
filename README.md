# Lora Lyco Classifier

日本語の説明は英語の後にあります。

This Python script classifies "LORA" and "LyCORIS" based on the 'model type' mentioned in `.civitai.info` files present in the same directory as the script.

Use of [Stable-Diffusion-Webui-Civitai-Helper extension](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper) is a prerequisite.


## How it works

The script operates in the following manner:

1. It scans all files in its current directory, which is the same directory where the script is located.

2. The script determines whether the 'model type' in the `.civitai.info` file is 'LORA' or 'LyCORIS'.

3. The script creates directories named 'LORA' and 'LyCORIS'.

4. Based on the 'model type', files are moved to their respective 'LORA' or 'LyCORIS' directory.

5. Once the process is completed, the script generates a log file named 'lora_lyco_classifier.log'.

## Usage

To use this script, simply place `lora_lyco_classifier.py` in the directory containing the `.civitai.info` files and other associated files such as `.safetensors` and `.preview.png`.

Run the script using Python 3. No additional arguments are required:

```python
python3 lora_lyco_classifier.py
```

After running the script, the files will be moved to the 'Lora' and 'LyCORIS' directories and a log file named 'lora_lyco_classifier.log' will be created in the same directory.


# Lora Lyco 分類器

このPythonスクリプトは、スクリプトと同じディレクトリに存在する`.civitai.info`ファイルに記載された'model type'に基づいて"LORA"と"LyCORIS"に分類します。

[Stable-Diffusion-Webui-Civitai-Helper extension](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper) の利用を前提にしています。

## 動作方法

スクリプトは次のように動作します：

1. スクリプトが存在するディレクトリ内のすべてのファイルをスキャンします。

2. `.civitai.info`ファイルの内容から'model type'が'LORA'または'LyCORIS'のいずれであるか判別します。

3. 'LORA' および 'LyCORIS' ディレクトリを作成します。

4. 'model type'に基づき'LOAR', 'LyCORIS'ファイルをそれぞれのディレクトリに移動します。

5. 処理が完了したら、'lora_lyco_classifier.log'という名前のログファイルを生成します。

## 使い方

シンプルに`lora_lyco_classifier.py`を`.civitai.info`ファイルとその他の関連ファイル（`.safetensors`や`.preview.png`）を含むディレクトリに配置してください。

Python 3を使用してスクリプトを実行します。追加の引数は必要ありません：

```Python
python3 lora_lyco_classifier.py
```

スクリプトを実行すると'Lora'と'LyCORIS'ディレクトリにファイルが移動し、'lora_lyco_classifier.log'というログファイルが作成されます。
