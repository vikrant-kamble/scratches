"""
Utility script to create a Mock Segmentation campaign.

The prime use is to test new development in gt_automation - selecting
AOIs for additional vote collection based on some ranking (complexity) metric.
"""

from data_science_tools.gt_campaign import LabelboxCampaign
import textwrap


def main():
    campaign_config = f"""
        name: "GT Tooling Mock campaign - Segmentation"
        project: "gt_tooling"
        description: "GT Tooling Mock campaign - Segmentation"
        gt_manager: "Sikha Das"
        project_lead: "Vikrant Kamble"
        datasets: 
            - class: TileSet
              mnemonic: vexcel_tree/20201020_high_campaign2_v1
              min_zoom: 17
              max_zoom: 21
              padding_zoom: 21
              padding: 1

        ticket: "DS-000"
        frontend: "https://image-segmentation-v4.labelbox.com"
        ontology: 

            - segmentation:
                taxonomy: "tree @ 1.0: ground_truth"
                object_type: polygon

            - segmentation:
                taxonomy: "roof @ 1.0: ground_truth"
                object_type: polygon

                questions:

                    - classification:
                        instructions: "Indicate one or more roof geometries"
                        taxonomy: "roof_geometry @ 2.0: ground_truth"
                        required: true
                        question_type: checklist

            """

    lc = LabelboxCampaign.from_config(textwrap.dedent(campaign_config))
    lc.create()


if __name__ == '__main__':
    main()
