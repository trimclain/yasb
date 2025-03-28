DEFAULTS = {
    'label_offline': 'Komorebi Offline',
    'label_workspace_btn': '{index}',
    'label_workspace_active_btn': '{index}',
    'label_workspace_populated_btn': '{index}',
    'label_default_name': '',
    'label_float_override': 'Override Active',
    'toggle_workspace_layer': {'enabled': False, 'tiling_label': "Tiling", 'floating_label': "Floating"},
    'hide_if_offline': False,
    'label_zero_index': False,
    'hide_empty_workspaces': False,
    'animation': False,
    'container_padding': {'top': 0, 'left': 0, 'bottom': 0, 'right': 0},
}

VALIDATION_SCHEMA = {
    'label_offline': {
        'type': 'string',
        'default': DEFAULTS['label_offline']
    },
    'label_workspace_btn': {
        'type': 'string',
        'default': DEFAULTS['label_workspace_btn']
    },
    'label_workspace_active_btn': {
        'type': 'string',
        'default': DEFAULTS['label_workspace_active_btn']
    },
    'label_workspace_populated_btn': {
        'type': 'string',
        'default': DEFAULTS['label_workspace_populated_btn']
    },
    'label_default_name': {
        'type': 'string',
        'default': DEFAULTS['label_default_name']
    },
    'label_float_override': {
        'type': 'string',
        'default': DEFAULTS['label_float_override']
    },
    'toggle_workspace_layer': {
        'type': 'dict',
        'default': DEFAULTS['toggle_workspace_layer'],
        'schema': {
            'enabled': {
                'type': 'boolean',
                'default': DEFAULTS['toggle_workspace_layer']['enabled']
            },
            'tiling_label': {
                'type': 'string',
                'default': DEFAULTS['toggle_workspace_layer']['tiling_label']
            },
            'floating_label': {
                'type': 'string',
                'default': DEFAULTS['toggle_workspace_layer']['floating_label']
            }
        }
    },
    'hide_if_offline': {
        'type': 'boolean',
        'default': DEFAULTS['hide_if_offline']
    },
    'label_zero_index': {
        'type': 'boolean',
        'default': DEFAULTS['label_zero_index']
    },
    'hide_empty_workspaces': {
        'type': 'boolean',
        'default': DEFAULTS['hide_empty_workspaces']
    },
    'animation': {
        'type': 'boolean',
        'default': DEFAULTS['animation']
    },
    'container_padding': {
        'type': 'dict',
        'default': DEFAULTS['container_padding'],
        'required': False
    }
}
