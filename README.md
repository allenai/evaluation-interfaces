# Evaluation Interfaces for Generative Models
This repository is intended as a central hub for interfaces that support evaluation of generative model outputs.
For more motivation on why this is important, see [our recent paper](https://arxiv.org/abs/2101.06561) on how to simplify evaluation of generative models.
The [Genie leaderboard](https://genie.apps.allenai.org/) leverages interfaces in this repository.

The interfaces here use the formats accepted by the [amti](https://github.com/allenai/amti) library.

This is repository is a WiP. More interfaces will be added and contributing guidelines defined.

## Currently supported tasks
- [xsum](https://huggingface.co/datasets/xsum) (summarization)

## Getting started
Clone this repository, install python>=3.6, and run
- `pip install -r requirements.txt`

## Previewing an evaluation template
1. Obtain a model predictions file for the target dataset. To generate a sample `$DATASET-sample.json` predictions file, run `python src/make_sample_predictions --dataset $DATASET`.
2. Run `python src/process.py $DATASET-sample.json --dataset $DATASET` to produce `$DATASET-processed.jsonl`, which will be used to instantiate the evaluation tasks. You may substitute `$DATASET-sample.json` with your own predictions file.
2. Run `amti preview-batch templates/xsum/mturk-specs-likert $DATASET-processed.jsonl` to start a local web server to preview the evaluation tasks. (To view the first task, navigate to <http://127.0.0.1:8000/hits/0/>.)

Notes:
- Currently, the above instructions work only for `DATASET=xsum`.
- The xsum model predictions format is described [here](https://leaderboard.allenai.org/genie-xsum/submissions/get-started).
- New HIT templates should use the `jinja2` format, as in the `templates/xsum/mturk-specs-likert/question.xml.j2` example. For more details about how this format can be used in the [amti](https://github.com/allenai/amti) library for managing HITs on Amazon Mechanical Turk, see [those docs](https://github.com/allenai/amti#amti-concepts).
