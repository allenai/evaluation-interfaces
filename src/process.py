"""Process a model predictions file into a format for HIT consumption."""
from typing import TextIO, Optional
import json
import click
import tasks

MAX_SIZE = 10


@click.command()
@click.argument('predictions', type=click.File(mode='r'))
@click.option(
    '--dataset', '-d',
    type=click.Choice(['xsum']),
    default='xsum',
    help='Dataset name'
)
@click.option(
    '--output', '-o',
    type=click.Path(),
    default=None,
    help='Output path'
)
def process(predictions: TextIO, dataset: str, output: Optional[str]):
    """Process PREDICTIONS file for HIT consumption."""
    if output is None:
        output = f'{dataset}-processed.jsonl'
    task = tasks.tasks[dataset](max_size=MAX_SIZE)
    gold = task.process_predictions(json.load(predictions))
    with open(output, 'w', encoding='utf-8') as f:
        f.writelines(json.dumps(d) + '\n' for d in gold)


if __name__ == '__main__':
    process()
