#!/usr/bin/env python3
# -*- coding: utf-8 -*-


data_compare_standard = {
    'Sharpness': {
        '1000lux': {
            'Rear': 2100,
            'Front': 1600
        },
        '35lux': {
            'Rear': 1800,
            'Front': 900
        }
    },
    'CA': {
        '1000lux': {
            'Rear': 1
        }
    },
    'Flash': {
        'Max Pixel Level': {
            'Rear 1M': 0.6,
            'Rear 2M': 0.55
        },
        'Corner Worst': {
            'Rear 1M': 0.4,
            'Rear 2M': 0.35
        },
        'Sides Worst': {
            'Rear 1M': 0.5,
            'Rear 2M': 0.5
        }

    },
    'Shading': {
        'Corner Worst': {
            'Rear': 0.9,
            'Front': 0.9
        },
        'Sides Worst': {
            'Rear': 0.9,
            'Front': 0.9
        },
        'Max delta C': {
            'Rear': 2,
            'Front': 2
        }
    },
    'Color': {
        'A 1000lux': {
            'Sat': {
                'Rear_up': 1.0,
                'Rear_down': 1.3,
                'Front_up': 0.8,
                'Front_down': 1.1
            },
            'delta E 00': {
                'Rear': 9,
                'Front': 12
            },
            'AWB': {
                'Rear': 5,
                'Front': 10
            }
        },
        'A 35lux': {
            'Sat': {
                'Rear_up': 1.0,
                'Rear_down': 1.3,
                'Front_up': 0.7,
                'Front_down': 1.0
            },
            'delta E 00': {
                'Rear': 8,
                'Front': 12
            },
            'AWB': {
                'Rear': 7,
                'Front': 10
            }
        },
        'D65 1000lux': {
            'Sat': {
                'Rear_up': 1.0,
                'Rear_down': 1.3,
                'Front_up': 1.0,
                'Front_down': 1.3
            },
            'delta E 00': {
                'Rear': 8,
                'Front': 10
            },
            'AWB': {
                'Rear': 5,
                'Front': 7
            }
        },
        'D65 35lux': {
            'Sat': {
                'Rear_up': 1.0,
                'Rear_down': 1.3,
                'Front_up': 1.0,
                'Front_down': 1.3
            },
            'delta E 00': {
                'Rear': 8,
                'Front': 10
            },
            'AWB': {
                'Rear': 5,
                'Front': 7
            }
        }
    },
    'Noise': {
        '1000lux': {
            'RGBY': {
                'Rear': 38,
                'Front': 30
            },
            'Gamma': {
                'Rear': 0.6
            }
        },
        '10lux': {
            'RGBY': {
                'Rear': 30,
                'Front': 25
            },
            'Gamma': {
                'Rear': 0.8
            }
        }
    },
    'DR': {
        'SNR1': {
            'Rear': 58,
            'Front': 58
        },
        'SNR10': {
            'Rear': 33,
            'Front': 33
        }
    }
}