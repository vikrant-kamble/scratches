from data_science_tools.aoi_selection_tool import AoiPipeline
from data_science_tools.aoi_selection_tool.sqlalchemy_wrappers import BaseWrapper
from data_science_tools.aoi_selection_tool.frontend_components import *


def main():
    primary = Primary(
        kind="attributes",
        imagery_refresh="2018-02",
        optional_cols=["state", "yearbuilt"],
    )

    cape = CapeAttributes(
        constraints={
            "cape_roof_condition_rating": ["-1"],
            "cape_roof_geometry": "gable",
        }
    )

    attom = Attom(
        constraints={"propertyusestandardized":
                         ["382", "383", "385"]}
    )

    pipeline = AoiPipeline([primary, cape, attom])
    _ = pipeline.run(n_samples=1000, query_only=True, fetch_geometries=False)

    print(pipeline.sql_query[0])


def main2():
    # We want a pool of attribute geometries that have roofmaterial wood shake shingle

    primary = Primary(
        kind='attributes',
        imagery_refresh='2018-02'
    )

    cape = CapeAttributes(
        constraints={
            "num_attom_matches": 1,
            "largest_structure": True
        }
    )

    attom = Attom(
        constraints={
            "roofmaterial": ['103', '127', '135', '136',
                             '137', '138', '139', '140', '142']
        }
    )

    pipeline = AoiPipeline([primary, cape, attom])

    raw_sql, df = pipeline.run(n_samples=1000, query_only=True, fetch_geometries=True)
    print(raw_sql)
    
    
def main3():
    # This query was giving resources exhausted for Jonathan - improve this !!!
    components = [
        Primary(kind="primary_roof", imagery_refresh='2018-02', optional_cols=["parcel_geometry_id"]),
        Attom(constraints={
            "propertyusestandardized": ["382", "383", "385"]
                           },

    ),
        Stratify(columns=['state'], balanced=True, objects_per_strata=100)
    ]

    pipeline = AoiPipeline()
    pipeline.add_components(components)
    pipeline.run(query_only=True, fetch_geometries=False)

    # print(query)


def test():
    # This query was giving resources exhausted for Jonathan - improve this !!!
    components = [
        Primary(kind="primary_roof", 
                imagery_refresh='2018-02', 
                optional_cols=["parcel_geometry_id"]),
        Attom(constraints={
            "propertyusestandardized": ["382", "383", "385"]
                           }),
        # Stratify(columns=['state'], balanced=True, objects_per_strata=100)
        Stratify(columns=['state'], balanced=False)
    ]

    pipeline = AoiPipeline()
    pipeline.add_components(components)
    _ = pipeline.run(n_samples=1000, query_only=True, fetch_geometries=True)

    qrs = pipeline.sql_query

    for qr in qrs:
        print(qr)
    # print(pipeline.sql_query[0])


if __name__ == "__main__":
    main()
    # test()

