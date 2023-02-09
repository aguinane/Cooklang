# Cooklang

Python Cooklang parser.


## Export to other formats

If you pass a folder full of cook recipes, it will export to the markdown format needed to make use of one of these two static website projects:
- [nyum](https://github.com/doersino/nyum)
- [chowdown](https://github.com/clarklab/chowdown)

Simply specify the folder of the recipes and output folder:

```sh
python -m cooklang to-chowdown recipes chowdown
python -m cooklang to-nyum recipes nyum
```

It can also import from nyum markdown (with limited success):

```sh
python -m cooklang from-nyum nyum recipes
```