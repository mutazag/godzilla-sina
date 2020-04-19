<!-- TOC -->autoauto- [1. download files](#1-download-files)auto- [2. install 7z tools](#2-install-7z-tools)auto- [3. unzip files](#3-unzip-files)auto- [4. Meta](#4-meta)auto- [data explorer for stack exchange](#data-explorer-for-stack-exchange)autoauto<!-- /TOC -->
# 1. download files 

Files can be downloaded from the archives: (https://archive.org/download/stackexchange).


EDA on the gaming stack excahnge files; [gaming files](https://archive.org/download/stackexchange/gaming.stackexchange.com.7z) and [gaming meta](https://archive.org/download/stackexchange/gaming.meta.stackexchange.com.7z).
# 2. install 7z tools 

to install 7z tools on ubuntu (I use ubuntu on WSL)

```
sudo apt install p7zip-full p7zip-rar
```

# 3. unzip files
to unzip

```
7z e gaming.meta.stackexchange.com.7z  -ogaming/meta
7z e gaming.stackexchange.com.7z  -ogaming
```


# 4. Meta

[Stack Exchange Metadata Details](stackexchange_meta.txt)

# data explorer for stack exchange 

[Stack Exchange Data Explorer](https://data.stackexchange.com/)