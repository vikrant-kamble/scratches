WITH T AS
         (
             SELECT partner,
                    uuid,
                    addressfull,
                    state,
                    cy,
                    poleffdate,
                    earnedprem,
                    total_claim_loss,
                    total_loss_ratio,
                    bool_loss
             FROM loss_exposure.partner_data
             WHERE total_claim_loss >= 10000
               AND eed >= 360
               AND earnedprem >= 0
         )
SELECT T.partner
     , T.uuid
     , T.addressfull
     , T.state
     , T.cy
     , T.poleffdate
     , cd.attribute_geometry_id
     , cd.cape_parcel_id
     , cd.cape_structure_footprint_sqft
     , cd.cape_parcel_area_sqft
     , cd.cape_wildland_proximity
     , cd.cape_pool_enclosure
     , cd.cape_pool_presence
     , cd.cape_roof_condition_rating
     , cd.cape_roof_covering
     , cd.cape_roof_extension
     , cd.cape_roof_geometry
     , cd.cape_roof_occlusion
     , cd.cape_roof_solar_panel
     , cd.cape_tree_overhang
     , cd.cape_vegetation_coverage_zone_1
     , cd.cape_vegetation_coverage_zone_2
     , cd.cape_vegetation_coverage_zone_3
     , cd.cape_vegetation_setback_ft
     , cd.cape_wildfire_hazard_potential
     , cd.cape_yard_debris_coverage_pct
     , cd.cape_yard_debris_coverage_sqft
     , T.earnedprem
     , T.total_claim_loss
     , T.total_loss_ratio
     , T.bool_loss
from T
         JOIN loss_exposure.cape_data AS cd
              ON T.uuid = cd.uuid;