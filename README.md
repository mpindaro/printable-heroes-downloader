# Printable Heroes Mini Downloader

This script downloads Printable Heroes miniatures in PDF format. It requires a valid authorization bearer to be provided and supports setting the tier to download.

## Usage

To use this script, you will need to have Python 3 installed. You can then clone the repository and install the required packages:

```bash
git clone https://github.com/username/printable-heroes-mini-downloader.git
cd printable-heroes-mini-downloader
pip install -r requirements.txt
```

Once you have installed the required packages, you can run the script with the following command:
```bash
python printable_heroes_downloader.py --authorization <authorization code> --tier <tier>
```

Replace `<authorization code>` with your own authorization bearer (excluding _"Bearer "_) and `<tier>` with the desired tier to download. By default, the script will attempt to download all miniatures in tiers 1-3.

The script will create a directory called `downloaded_files` in the current directory and download each miniature to a subdirectory named after the miniature. 
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.