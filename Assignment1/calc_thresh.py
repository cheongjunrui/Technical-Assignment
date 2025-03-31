def find_best_threshold(metrics):
    """
    Find the threshold with highest precision among those meeting recall ≥ 0.9

    Args:
        metrics: List of dictionaries containing classification metrics.
                Format: [{'threshold': float, 'tp': int, 'tn': int, 'fp': int, 'fn': int}, ...]

    Returns:
        Best threshold (float) or None if no valid threshold exists
    """
    best_threshold = None
    best_precision = -1.0

    for entry in metrics:
        tp = entry['tp']
        fn = entry['fn']
        fp = entry['fp']

        # Calculate recall and skip if < 0.9
        recall_denominator = tp + fn
        recall = tp / recall_denominator if recall_denominator else 0.0
        if recall < 0.9:
            continue

        # Calculate precision
        precision_denominator = tp + fp
        precision = tp / precision_denominator if precision_denominator else 0.0

        # Update best if current precision is better, or equal precision with higher threshold
        if (precision > best_precision) or \
                (precision == best_precision and entry['threshold'] > best_threshold):
            best_precision = precision
            best_threshold = entry['threshold']

    return best_threshold if best_threshold is not None else None


# Test with realistic data
def test():
    sample_metrics = [
        {'threshold': 0.1, 'tp': 950, 'tn': 100, 'fp': 900, 'fn': 50},
        {'threshold': 0.5, 'tp': 920, 'tn': 500, 'fp': 500, 'fn': 80},
        {'threshold': 0.6, 'tp': 910, 'tn': 700, 'fp': 300, 'fn': 90},
        {'threshold': 0.7, 'tp': 900, 'tn': 800, 'fp': 200, 'fn': 100},
        {'threshold': 0.8, 'tp': 850, 'tn': 900, 'fp': 100, 'fn': 150},
    ]

    best_thresh = find_best_threshold(sample_metrics)
    print(f"Best threshold that yields a recall >= 0.9 : {best_thresh}")


if __name__ == "__main__":
    test()

