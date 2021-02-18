"""Make a sample model predictions file."""
from typing import Optional
import json
import click
from datasets import load_dataset


@click.command()
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
    help='Output path',
)
def make_sample_predictions(dataset: str, output: Optional[str]):
    """Create a sample model output."""
    if output is None:
        output = f'{dataset}-sample.json'
    if dataset == 'xsum':
        d = load_dataset(dataset)
        predictions = {
            x['id']: f'Machine-generated summmary for {x["id"]}'
            for x in d['test']
        }
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(predictions, f)
    else:
        raise NotImplementedError


if __name__ == '__main__':
    make_sample_predictions()
