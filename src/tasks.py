from typing import Dict, List
from pathlib import Path
from datasets import load_dataset

ROOT_DIR = Path(__file__).parent.parent


class XSUMTask:
    name = 'xsum'
    definition_dir = ROOT_DIR / 'templates' / 'xsum' / 'mturk-specs-likert'

    metrics = [
        'concise',
        'fluent',
        'hallucinate',
        'informative',
        'overall',
    ]

    def __init__(self, max_size):
        '''
        :param max_size: the number of instances we will evaluate on
        '''
        self.max_size = max_size

    def process_predictions(self, predictions: Dict) -> List[Dict]:
        dataset = load_dataset('xsum')
        gold = []
        for i, x in enumerate(dataset['test']):
            if i >= self.max_size:
                break
            try:
                gold.append(
                    {
                        'hash': x['id'],
                        'reference_pp': x['summary'],
                        'decoded_pp': predictions[x['id']],
                        'gold_story': x['document']
                    }
                )
            except KeyError:
                raise ValueError('Predictions file missing examples or has malformed examples')
        return gold


tasks = {
    'xsum': XSUMTask,
}
