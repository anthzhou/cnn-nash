se_init_config = {

    'conv1': {'config': {'in_channels': 3, 'out_channels': 64, 'kernel_size': 3, 'padding': 1, 'stride': 1},
              'inbound_nodes': ['input']},
    'bn1': {'config': {'input_size': 64}, 'inbound_nodes': ['conv1']},
    'relu1': {'config': '', 'inbound_nodes': ['bn1']},

    'max_pooling1': {'config': {'kernel_size': 2, 'stride': 2}, 'inbound_nodes': ['relu1']},

    'conv2': {'config': {'in_channels': 64, 'out_channels': 128, 'kernel_size': 3, 'padding': 1, 'stride': 1},
              'inbound_nodes': ['max_pooling1']},
    'bn2': {'config': {'input_size': 128}, 'inbound_nodes': ['conv2']},
    'relu2': {'config': '', 'inbound_nodes': ['bn2']},

    'max_pooling2': {'config': {'kernel_size': 2, 'stride': 2}, 'inbound_nodes': ['relu2']},

    'conv3': {'config': {'in_channels': 128, 'out_channels': 256, 'kernel_size': 3, 'padding': 1, 'stride': 1},
              'inbound_nodes': ['max_pooling2']},
    'bn3': {'config': {'input_size': 256}, 'inbound_nodes': ['conv3']},
    'relu3': {'config': '', 'inbound_nodes': ['bn3']},

    'fc1': {'config': {'input_size': 256*8*8, 'output_size': 10}, 'inbound_nodes': ['relu3']},
}