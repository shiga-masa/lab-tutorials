# 架空データ（練習用）

**このフォルダ（`qgis/data/` 全体）のデータはすべて架空です（synthetic, not real observations）。** 実際の観測・測量・調査の結果ではありません。
位置は新潟市付近に置いていますが、海岸線・川・土地被覆・液状化ポリゴン・観測点・変位の値はすべて計算で作ったものです。
観測点の番号（999901〜999904）・名前（架空A〜D）も実在しません。ファイル名の頭の `kaku_` は「架空」の意味です。
GeoTIFF と GeoPackage のメタデータにも `DESCRIPTION=架空データ（synthetic, not real observations）` を書いています。

- InSAR 風のラスタ: EPSG:4326、経度 139.0〜139.12°E、緯度 37.86〜37.96°N、画素 0.0004° × 0.000125°（300 列 × 800 行）
- 期間の名前（地震前・地震前後・地震後）は練習の設定に合わせただけで、値はすべて合成です。

## common/（各回で共通に使うデータ）

| ファイル | 内容 |
|---|---|
| `kaku_los_cum_pre_20231009_20231208_mm.tif` | 累積 LOS 変位（mm、正 = 衛星に近づく）地震前 2023-10-09〜2023-12-08。float32、NoData -9999 |
| `kaku_los_cum_co_20231208_20240101_mm.tif` | 同 地震前後 2023-12-08〜2024-01-01 |
| `kaku_los_cum_post_20240101_20240921_mm.tif` | 同 地震後 2024-01-01〜2024-09-21。液状化ポリゴンの内側ほど負 |
| `kaku_tempcoh.tif` | 時間コヒーレンス 0〜1。float32、NoData -9999（水域） |
| `kaku_mask_tempcoh.tif` | tempcoh >= 0.7 を 1。Byte、NoData なし |
| `kaku_velocity_std_mm_yr.tif` | 速度の標準偏差（mm/yr）。float32、NoData -9999 |
| `kaku_lulc_2020_west.tif / kaku_lulc_2020_east.tif` | 土地被覆（Byte、NoData 0、1/12,000 度、経度 139.06 で 2 枚）。クラス番号は JAXA 高解像度土地利用土地被覆図 v25.04 の凡例と同じ番号（使うクラス: 1 水域, 2 人工構造物, 3 水田, 4 畑地, 5 草地, 6 落葉広葉樹林, 10 裸地）。値は架空で、JAXA のデータは使っていません |
| `kaku_liq_polygons_6676.gpkg` | 液状化ポリゴン 12 個（レイヤ kaku_liq_polygons、EPSG:6676、列 区域・分類・note） |
| `kaku_study_area_32654.gpkg` | 調査範囲 1 個（レイヤ kaku_study_area、EPSG:32654） |
| `kaku_gnss_stations.csv` | GNSS 局 4 点（UTF-8、列 id,name,lat,lon,height_m,rmse_mm。緯度経度は EPSG:4326） |
| `kaku_gnss_stations_4326.gpkg` | 同じ 4 点の GeoPackage（レイヤ kaku_gnss_stations、EPSG:4326） |
| `kaku_999901.pos` | 局 999901 の日々の座標 60 日分（空白区切り、先頭 3 行がコメント、4 行目が列名） |
| `kaku_gnss_daily_999901.csv` | 上と同じ値の CSV |

## LQMNN/（その回の開始プロジェクトと、前の回までの処理結果）

| ファイル | 内容 |
|---|---|
| `LQMNN/kaku_LQMNN_start.qgz` | その回の開始プロジェクト（LQM02〜LQM18。相対パスで `../common/` などを読む） |
| `LQM03/kaku_liq_polygons_32654.gpkg` | 液状化ポリゴンを EPSG:32654 に再投影したもの（LQM02 の結果） |
| `LQM05/kaku_liq_dissolved_32654.gpkg`・`kaku_liq_dissolved_4326.gpkg` | 融合したポリゴン（LQM04 の結果）と、その EPSG:4326 版 |
| `LQM06/kaku_zone_poly_4326.tif` | ポリゴンを InSAR の格子でラスタ化したもの（中 = 1。LQM05 の結果） |
| `LQM06/kaku_zone_n1.tif`〜`kaku_zone_n3.tif` | 4 近傍で n 画素（n = 1, 2, 3）広げ・縮めたゾーン。値 1 コア・2 内縁・3 外縁・4 外側 |
| `LQM07/kaku_zone_poly.tif`・`kaku_grow_n1.tif`・`kaku_growc_n1.tif` | ラスタ計算機の入力（0/1 のラスタ: ポリゴン、ポリゴンを 1 画素広げたもの、ポリゴンの外を 1 画素広げたもの） |
| `LQM13/kaku_zone_stats_n1.gpkg` | ゾーンごとのコヒーレンスの統計の表（LQM12 の結果） |
| `LQM15/kaku_lulc_clip.tif` | 結合して調査範囲で切り抜いた土地被覆（LQM14 の結果） |
| `LQM16/kaku_lulc_grid.tif` | 土地被覆を InSAR の格子にそろえたもの（LQM15 の結果） |
