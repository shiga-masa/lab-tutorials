# 研究室 QGIS（LQM01〜LQM18）

卒業論文で InSAR の結果を整理する学生向けの、QGIS の基本操作を 1 回 1 機能で練習する動画講座の教材です。レイヤの読み込み・座標系・ラスタ化・ラスタ計算機・再分類・スタイル・印刷レイアウト・ゾーン統計・CSV の読み込みなど 18 の操作を扱います。

- 動作確認: QGIS 3.34.4（Ubuntu 24.04）。メニューやツールの名前は 3.34.4 の日本語表示です。
- 練習用データは架空です（下の「データについて」）。

## 動画

YouTube の再生リスト（限定公開）: https://www.youtube.com/playlist?list=PLASyjI-Dpl68

各回の動画は下の表の「動画」の列から開けます。

## 各回と開始プロジェクト

各回は、その回用の開始プロジェクトを QGIS で開いた状態から始まります（LQM01 だけは空の QGIS から始めます）。

| 回 | 題名 | 動画 | 開始プロジェクト |
|---|---|---|---|
| LQM01 | レイヤを読み込んでプロジェクトを保存する | [動画](https://youtu.be/VPpze233yvY) | なし（空の QGIS で [`data/common/`](data/common/) の `kaku_tempcoh.tif` と `kaku_liq_polygons_6676.gpkg` を読み込む） |
| LQM02 | 座標系を UTM 54N にそろえる | [動画](https://youtu.be/2ypPaJvMu_8) | [`data/LQM02/kaku_LQM02_start.qgz`](data/LQM02/) |
| LQM03 | 画素の値とラスタの情報を見る | [動画](https://youtu.be/9l5j0rCHfvc) | [`data/LQM03/kaku_LQM03_start.qgz`](data/LQM03/) |
| LQM04 | ポリゴンを融合して 1 つにする | [動画](https://youtu.be/fCQdQFXxG_4) | [`data/LQM04/kaku_LQM04_start.qgz`](data/LQM04/) |
| LQM05 | ポリゴンを InSAR の格子でラスタ化する | [動画](https://youtu.be/azQE4jehbaE) | [`data/LQM05/kaku_LQM05_start.qgz`](data/LQM05/) |
| LQM06 | Python で作ったゾーンを QGIS で確かめる | [動画](https://youtu.be/x_McdGlV3Ls) | [`data/LQM06/kaku_LQM06_start.qgz`](data/LQM06/) |
| LQM07 | ラスタ計算機でゾーンを作る | [動画](https://youtu.be/yoidspURQHE) | [`data/LQM07/kaku_LQM07_start.qgz`](data/LQM07/) |
| LQM08 | 区分表で 3 段階に再分類する | [動画](https://youtu.be/ylc8IXK5ByU) | [`data/LQM08/kaku_LQM08_start.qgz`](data/LQM08/) |
| LQM09 | 変位を 0 中心の 2 色で表示する | [動画](https://youtu.be/MVS1NeH4a8k) | [`data/LQM09/kaku_LQM09_start.qgz`](data/LQM09/) |
| LQM10 | 輪郭だけのポリゴンと色分けした点 | [動画](https://youtu.be/y9BIeaKDTb0) | [`data/LQM10/kaku_LQM10_start.qgz`](data/LQM10/) |
| LQM11 | 印刷レイアウトで図を書き出す | [動画](https://youtu.be/kzfODEG-VHI) | [`data/LQM11/kaku_LQM11_start.qgz`](data/LQM11/) |
| LQM12 | ゾーンごとの統計を出す | [動画](https://youtu.be/j4hubG-uuOA) | [`data/LQM12/kaku_LQM12_start.qgz`](data/LQM12/) |
| LQM13 | 属性テーブルを見て CSV に書き出す | [動画](https://youtu.be/T4GaGTGSzx0) | [`data/LQM13/kaku_LQM13_start.qgz`](data/LQM13/) |
| LQM14 | タイルを結合して範囲で切り抜く | [動画](https://youtu.be/BjuYUXHjH7M) | [`data/LQM14/kaku_LQM14_start.qgz`](data/LQM14/) |
| LQM15 | 土地被覆を InSAR の格子にそろえる（モード） | [動画](https://youtu.be/oeJJ624f7mE) | [`data/LQM15/kaku_LQM15_start.qgz`](data/LQM15/) |
| LQM16 | ポリゴンごとの土地被覆（最頻値） | [動画](https://youtu.be/ai1j9t_9O38) | [`data/LQM16/kaku_LQM16_start.qgz`](data/LQM16/) |
| LQM17 | CSV の観測点を地図に載せる | [動画](https://youtu.be/UsJRSKZh81Q) | [`data/LQM17/kaku_LQM17_start.qgz`](data/LQM17/) |
| LQM18 | 範囲の中の観測点だけを選ぶ | [動画](https://youtu.be/fFn8wb0ZNmI) | [`data/LQM18/kaku_LQM18_start.qgz`](data/LQM18/) |

## 使い方

1. このリポジトリをダウンロードします（GitHub の「Code」→「Download ZIP」を展開する、または `git clone https://github.com/shiga-masa/lab-tutorials.git`）。
2. **`qgis/data/` の中のフォルダ構成を変えずに** 使ってください。開始プロジェクトは相対パスで `../common/` や `../LQM03/` などのファイルを読み込むので、`kaku_LQMNN_start.qgz` だけを別の場所に移すとレイヤが見つからなくなります。
3. QGIS で「プロジェクト」→「開く…」から、その回の `data/LQMNN/kaku_LQMNN_start.qgz` を開きます（ファイルをダブルクリックしても開けます）。
4. 動画と同じ手順で操作します。処理の出力は動画と同じく「一時ファイル」にしておけば、元のデータは変わりません。

## データについて

**ここにあるデータはすべて架空です（synthetic, not real observations）。** 実際の観測・測量・調査の結果ではありません。位置は新潟市付近に置いていますが、海岸線・川・土地被覆・液状化ポリゴン・観測点・変位の値はすべて計算で作ったものです。ファイル名の頭の `kaku_` は「架空」の意味で、GeoTIFF と GeoPackage のメタデータにも架空データであることを書いています。

ファイルの一覧と中身は [`data/common/README_架空データ.md`](data/common/README_架空データ.md) にあります。

## QGIS について

QGIS は QGIS プロジェクトが開発するフリー・オープンソースのソフトウェアです。公式サイト: https://qgis.org

この教材は QGIS プロジェクトとは関係がなく、QGIS プロジェクトの承認を受けたものではありません。

## ライセンス

データと文書は CC BY 4.0 です（リポジトリ直下の [`README.md`](../README.md) と [`LICENSE-CC-BY-4.0`](../LICENSE-CC-BY-4.0)）。
