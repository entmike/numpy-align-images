# numpy-align-images

# Examples

Run CPU:

```bash
docker run -it --rm -v $PWD/in:/in -v $PWD/aligned:/aligned entmike/align-images:cpu
```

Run GPU:

```bash
docker run -it --rm -v $PWD/in:/in -v $PWD/aligned:/aligned entmike/align-images:gpu
```