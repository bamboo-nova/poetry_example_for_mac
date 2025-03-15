# Abstruct
macでもpoetryを使って深層学習ライブラリの開発環境を構築する方法

# Usage

1. .envのコピー

```
$ cd chiikawa
$ cp .env{.example,}
```

2. dockerイメージの構築

```
$ DOCKER_BUILDKIT=1 docker build . -t poetry-example
```

3. コンテナの起動

```
$ docker compose run --rm poetry-demo
```