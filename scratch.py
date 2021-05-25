from data_science_tools.tile_servers import ShowerV2
from data_science_tools.data_sources import APISource
from data_science_tools.core import refresh_configuration
from data_science_tools.datasets import AttrGeomSet
from data_science_tools.geometry import wkb_to_shapely


def main():

    refresh_configuration()

    sv2 = ShowerV2()
    #
    # surveys_1 = sv2.get_available_surveys(X=286100, Y=431821, Z=20, datatype_name='nearmap_vertical_jpg')
    # print(surveys_1)

    surveys_2 = sv2.get_surveys_covering_area(21, 365858, 365898, 846848, 846948, 2, 2)
    # surveys_2 = sv2.get_surveys_covering_area(21, 365858, 365898, 846848, 846948, 2, 2,
    #                                       datatype_name='nearmap_vertical_jpg')
    print(surveys_2.shape)
    print(surveys_2['datatype_name'].value_counts())

    # blk = APISource.from_mnemonic('blanket')
    # blk.describe()


def main2():
    ds = AttrGeomSet.from_mnemonic('rcrv4/20201016_internal_campaign_test')
    df = ds.to_pandas()

    sub_df = df.sample(100, replace=False).reset_index()
    sub_df.rename(columns={"polygon": "geometry"}, inplace=True)

    # Convert geometry to Shapely - is this needed?
    sub_df["geometry"] = sub_df["geometry"].apply(wkb_to_shapely)

    sv2 = ShowerV2()

    df_with_nearmap = sv2.get_best_surveys_geom(geom=sub_df['geometry'],
                                                query_params={'datatype_name': 'nearmap_vertical_jpg'})
    print(df_with_nearmap.shape)

    print(df_with_nearmap.head())

    print(df_with_nearmap['datatype_name'].value_counts())


if __name__ == '__main__':
    # main()
    main2()
