# QGIS（#01〜#34）

卒業論文で InSAR の結果を整理する学生向けの、QGIS の基本操作を 1 回 1 機能で練習する動画講座の教材です。全 34 回で、用語の説明（16 回）を、その用語を使う操作（18 回）の前に置いています。操作の回では、レイヤの読み込み・座標系・ラスタ化・ラスタ計算機・再分類・スタイル・印刷レイアウト・ゾーン統計・CSV の読み込みなどを扱います。

- 動作確認: QGIS 3.34.4（Ubuntu 24.04）。メニューやツールの名前は 3.34.4 の日本語表示です。
- 練習用データは架空です（下の「データについて」）。

## 動画

YouTube の再生リスト（限定公開）: https://www.youtube.com/playlist?list=PLASyjI-Dpl68

各回の動画は下の表の「動画」の列から開けます。

## 各回と開始プロジェクト

操作の回は、その回用の開始プロジェクトを QGIS で開いた状態から始まります（#04 だけは空の QGIS から始めます）。用語の説明の回には練習用データはありません。

動画の画面に映るプロジェクト名（`kaku_LQM02_start` など）と #04 で保存するときの名前（`kaku_lqm01`）は、番号を振り直す前の旧番号です。旧番号 LQM01〜LQM18 は、下の表の「操作」の回に上から順に対応します（LQM01 = #04、LQM02 = #07、…、LQM18 = #34）。

| 回 | 題名 | 種類 | 動画 | 開始プロジェクト |
|---|---|---|---|---|
| #01 | GIS とレイヤ | 用語 | [動画](https://youtu.be/pi8Vy7PFSgk) | なし（用語の説明） |
| #02 | ラスタとベクタ | 用語 | [動画](https://youtu.be/KPcu6Zb5w7E) | なし（用語の説明） |
| #03 | ファイルとプロジェクト | 用語 | [動画](https://youtu.be/WnhonkkjNVE) | なし（用語の説明） |
| #04 | レイヤの読み込みとプロジェクトの保存 | 操作 | [動画](https://youtu.be/VPpze233yvY) | なし（空の QGIS で [`data/common/`](data/common/) の `kaku_tempcoh.tif` と `kaku_liq_polygons_6676.gpkg` を読み込む） |
| #05 | 座標参照系 | 用語 | [動画](https://youtu.be/8tkdz4-L2j8) | なし（用語の説明） |
| #06 | プロセシングツールボックス | 用語 | [動画](https://youtu.be/heX_OsE_7T0) | なし（用語の説明） |
| #07 | 座標系の UTM 54N への統一 | 操作 | [動画](https://youtu.be/hlCNrTMIYu8) | [`data/LQ07/kaku_LQ07_start.qgz`](data/LQ07/) |
| #08 | 画素と NoData | 用語 | [動画](https://youtu.be/m9m7a6rgHGc) | なし（用語の説明） |
| #09 | 地物と属性テーブル | 用語 | [動画](https://youtu.be/dz0CnqklWrk) | なし（用語の説明） |
| #10 | InSAR の変位とコヒーレンス | 用語 | [動画](https://youtu.be/a4qJdZxShDk) | なし（用語の説明） |
| #11 | 土地被覆・液状化ポリゴン・観測点 | 用語 | [動画](https://youtu.be/fOx8YPi4QYI) | なし（用語の説明） |
| #12 | 画素の値とラスタの情報の確認 | 操作 | [動画](https://youtu.be/9l5j0rCHfvc) | [`data/LQ12/kaku_LQ12_start.qgz`](data/LQ12/) |
| #13 | 融合・結合・切り抜き | 用語 | [動画](https://youtu.be/e401Wv7-l8I) | なし（用語の説明） |
| #14 | ポリゴンの 1 つへの融合 | 操作 | [動画](https://youtu.be/fCQdQFXxG_4) | [`data/LQ14/kaku_LQ14_start.qgz`](data/LQ14/) |
| #15 | ラスタ化と再サンプリング | 用語 | [動画](https://youtu.be/IjI4K2mphAs) | なし（用語の説明） |
| #16 | InSAR の格子でのポリゴンのラスタ化 | 操作 | [動画](https://youtu.be/azQE4jehbaE) | [`data/LQ16/kaku_LQ16_start.qgz`](data/LQ16/) |
| #17 | ラスタ計算機と再分類 | 用語 | [動画](https://youtu.be/R9EwfkmDGA4) | なし（用語の説明） |
| #18 | シンボロジ | 用語 | [動画](https://youtu.be/OIY3_518E4Q) | なし（用語の説明） |
| #19 | Python で作ったゾーンの QGIS での確認 | 操作 | [動画](https://youtu.be/x_McdGlV3Ls) | [`data/LQ19/kaku_LQ19_start.qgz`](data/LQ19/) |
| #20 | ラスタ計算機によるゾーンの作成 | 操作 | [動画](https://youtu.be/yoidspURQHE) | [`data/LQ20/kaku_LQ20_start.qgz`](data/LQ20/) |
| #21 | 区分表による 3 段階への再分類 | 操作 | [動画](https://youtu.be/ylc8IXK5ByU) | [`data/LQ21/kaku_LQ21_start.qgz`](data/LQ21/) |
| #22 | 0 中心の 2 色による変位の表示 | 操作 | [動画](https://youtu.be/MVS1NeH4a8k) | [`data/LQ22/kaku_LQ22_start.qgz`](data/LQ22/) |
| #23 | 輪郭だけのポリゴンと色分けした点 | 操作 | [動画](https://youtu.be/y9BIeaKDTb0) | [`data/LQ23/kaku_LQ23_start.qgz`](data/LQ23/) |
| #24 | 印刷レイアウト | 用語 | [動画](https://youtu.be/IU3rpIC_NF8) | なし（用語の説明） |
| #25 | 印刷レイアウトによる図の書き出し | 操作 | [動画](https://youtu.be/kzfODEG-VHI) | [`data/LQ25/kaku_LQ25_start.qgz`](data/LQ25/) |
| #26 | ゾーン統計 | 用語 | [動画](https://youtu.be/A-g-mB7etHc) | なし（用語の説明） |
| #27 | ゾーンごとの統計の算出 | 操作 | [動画](https://youtu.be/j4hubG-uuOA) | [`data/LQ27/kaku_LQ27_start.qgz`](data/LQ27/) |
| #28 | 属性テーブルの確認と CSV への書き出し | 操作 | [動画](https://youtu.be/T4GaGTGSzx0) | [`data/LQ28/kaku_LQ28_start.qgz`](data/LQ28/) |
| #29 | タイルの結合と範囲での切り抜き | 操作 | [動画](https://youtu.be/BjuYUXHjH7M) | [`data/LQ29/kaku_LQ29_start.qgz`](data/LQ29/) |
| #30 | 土地被覆の InSAR の格子への統一（モード） | 操作 | [動画](https://youtu.be/oeJJ624f7mE) | [`data/LQ30/kaku_LQ30_start.qgz`](data/LQ30/) |
| #31 | ポリゴンごとの土地被覆（最頻値） | 操作 | [動画](https://youtu.be/ai1j9t_9O38) | [`data/LQ31/kaku_LQ31_start.qgz`](data/LQ31/) |
| #32 | CSV の点レイヤ | 用語 | [動画](https://youtu.be/lBufv91JfVM) | なし（用語の説明） |
| #33 | CSV の観測点の地図への表示 | 操作 | [動画](https://youtu.be/UsJRSKZh81Q) | [`data/LQ33/kaku_LQ33_start.qgz`](data/LQ33/) |
| #34 | 範囲の中の観測点だけの選択 | 操作 | [動画](https://youtu.be/fFn8wb0ZNmI) | [`data/LQ34/kaku_LQ34_start.qgz`](data/LQ34/) |

## 使い方

1. このリポジトリをダウンロードします（GitHub の「Code」→「Download ZIP」を展開する、または `git clone https://github.com/shiga-masa/lab-tutorials.git`）。
2. **`qgis/data/` の中のフォルダ構成を変えずに** 使ってください。開始プロジェクトは相対パスで `../common/` や `../LQ12/` などのファイルを読み込むので、`kaku_LQNN_start.qgz` だけを別の場所に移すとレイヤが見つからなくなります。
3. QGIS で「プロジェクト」→「開く…」から、その回の `data/LQNN/kaku_LQNN_start.qgz` を開きます（`NN` は表の回の番号。ファイルをダブルクリックしても開けます）。
4. 動画と同じ手順で操作します。処理の出力は動画と同じく「一時ファイル」にしておけば、元のデータは変わりません。

## データについて

**ここにあるデータはすべて架空です（synthetic, not real observations）。** 実際の観測・測量・調査の結果ではありません。位置は新潟市付近に置いていますが、海岸線・川・土地被覆・液状化ポリゴン・観測点・変位の値はすべて計算で作ったものです。ファイル名の頭の `kaku_` は「架空」の意味で、GeoTIFF と GeoPackage のメタデータにも架空データであることを書いています。

ファイルの一覧と中身は [`data/common/README_架空データ.md`](data/common/README_架空データ.md) にあります。

## QGIS について

QGIS は QGIS プロジェクトが開発するフリー・オープンソースのソフトウェアです。公式サイト: https://qgis.org

この教材は QGIS プロジェクトとは関係がなく、QGIS プロジェクトの承認を受けたものではありません。

## ライセンス

データと文書は CC BY 4.0 です（リポジトリ直下の [`README.md`](../README.md) と [`LICENSE-CC-BY-4.0`](../LICENSE-CC-BY-4.0)）。
