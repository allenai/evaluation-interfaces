# Evaluation Interfaces for Generative Models
This repository is intended as a central hub for interfaces that support evaluation of generative model outputs.
For more motivation on why this is important, see [our recent paper](https://arxiv.org/abs/2101.06561) on how to simplify evaluation of generative models.
The [Genie leaderboard](https://genie.apps.allenai.org/) leverages interfaces in this repository.

The interfaces here use the jinja2 format accepted by the [amti](https://github.com/allenai/amti) library.

This is repository is a WiP. More interfaces will be added and contributing guidelines defined.

## Currently supported tasks
- [xsum](https://huggingface.co/datasets/xsum) (summarization)

## Getting started
Clone this repository, install python>=3.6, and run
- `pip install -r requirements.txt`

## Previewing an evaluation template
1. Obtain a model predictions file for the target dataset `$DATASET`. To generate a sample `$DATASET-sample.json` predictions file, run `python src/make_sample_predictions.py --dataset $DATASET`.
2. Run `python src/process.py $DATASET-sample.json --dataset $DATASET` to produce `$DATASET-processed.jsonl`, which will be used to instantiate the evaluation tasks. You may substitute `$DATASET-sample.json` with your own predictions file.
2. Run `amti preview-batch templates/$DATASET/$TEMPLATE $DATASET-processed.jsonl` to start a local web server to preview the evaluation tasks with the specified template `$TEMPLATE`. (To view the first task, navigate to <http://127.0.0.1:8000/hits/0/>.)

Notes:
- Currently, the above instructions work only for `DATASET=xsum` and `TEMPLATE=mturk-specs-likert`. We encourage development of additional templates for the xsum dataset, and will be expanding to additional datasets.
- The xsum model predictions file format is described [here](https://leaderboard.allenai.org/genie-xsum/submissions/get-started).
- New evaluation templates should use the jinja2 format, as in the `templates/xsum/mturk-specs-likert/question.xml.j2` example. Templates should be organized according to the `templates/$DATASET/$TEMPLATE` directory pattern. For more details about how evaluation templates can be used with the [amti](https://github.com/allenai/amti) tool for managing HITs on Amazon Mechanical Turk, see [those docs](https://github.com/allenai/amti#amti-concepts). The [Genie leaderboard](https://genie.apps.allenai.org/) handles model submissions and HIT management for hosted tasks.
