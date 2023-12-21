# Markfown ファイルの全角文字数カウント

## 実行方法
```
$ python src/markdown_fillwidth_counter.py filepath
```

## 数えない物
### 半角文字
```
abcあいう
```
3 文字  

```
3 文字
```
2 文字  

```
（　）  
```
3 文字．丸括弧と括弧の中の空白が全角．  

### ルビ
```
<ruby>漢字<rt>かんじ</rt></ruby>  
```
2 文字  

### 見出し
```
# 見出し
本文
```
2 文字  

### コメントアウトした文字
```
<!-- コメントアウトした文字は数えない -->
```
0 文字  

## その他
```
$ flake8 --version
6.1.0 (mccabe: 0.7.0, pycodestyle: 2.11.1, pyflakes: 3.1.0) CPython 3.10.12 on Linux
$ black --version
black, 23.11.0 (compiled: yes)
Python (CPython) 3.10.12
```
