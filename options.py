import argparse

def model_opts(parser):
    group = parser.add_argument_group('model')
    group.add_argument('-num_layers', type=int, default=4)
    group.add_argument('-word_vec_size', type=int, default=512)
    group.add_argument('-rnn_size', type=int, default=512)
    group.add_argument('-bidirectional_encoder', type=bool, default=True)
    group.add_argument('-attn_type', type=str, default='general')
    group.add_argument('-position_encoding', type=bool, default=True)
    group.add_argument('-head_count', type=int, default=8)
    group.add_argument('-transformer_hidden_size', type=int, default=2048)
    group.add_argument('-transformer_enc_layers', type=int, default=6)
    group.add_argument('-transformer_dec_layers', type=int, default=2)
    group.add_argument('-model_type', type=str, default='rnn')


def train_opts(parser):
    group = parser.add_argument_group('train')
    group.add_argument('-batch_size', type=int, default=64)
    group.add_argument('-learning_rate', type=float, default=0.001)
    group.add_argument('-dropout', type=float, default=0.3)
    group.add_argument('-using_gan', type=int, default=0)


def evaluate_opts(parser):
    group = parser.add_argument_group('evaluate')
    group.add_argument('-beam_size', type=int, default=5)
    group.add_argument('-max_length', type=int, default=20)
    group.add_argument('-min_length', type=int, default=5)
    group.add_argument('-batch_size', type=int, default=32)
    group.add_argument('-best_k_questions', type=int, default=3)
    group.add_argument('-output_file', type=str, default='./output/evaluate.txt')
    group.add_argument('-dropout', type=float, default=0)


