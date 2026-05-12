from random_samples import boxes
from random_samples import target_pdf

def test_boxes(xlim,
               n_boxes
               ):
    edges_left, edges_right, box_height = boxes(target_pdf,
                                            xlim,
                                            n_boxes
                                            )

    assert len(edges_left) == n_boxes
    assert len(edges_right) == n_boxes
    assert len(box_height) == n_boxes

    assert edges_left[0] == xlim[0]
    assert edges_right[-1] == xlim[1]

test_boxes(xlim=(0, 10), n_boxes=5)