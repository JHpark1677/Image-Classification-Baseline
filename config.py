import configargparse


def get_args_parser():
    # * config
    parser = configargparse.ArgumentParser(add_help=False)
    parser.add_argument("--path", default="D:\data", type=str,help='data path')
    parser.add_argument("--batch_size", default=128, type=int)
    parser.add_argument("--epoch_num", default=500, type=int)

    parser.add_argument("--dataset", default="cifar10", type=str)
    parser.add_argument("--resume",'-r',action='store_true', help='resume from checkpoint')
    parser.add_argument('--load_ckp',default='ckpt_vit.pth',type=str, help='checkpoint_name')
    parser.add_argument('--save_ckp',default='ckpt_vit.pth',type=str, help='checkpoint_name')

    parser.add_argument('--lr_backbone', default=1e-5, type=float)

    parser.add_argument('--visdom_true', action='store_true')
    parser.add_argument('--train_vis_step', type=int, default=100)
    parser.add_argument('--test_vis_step', type=int, default=100)

    parser.add_argument('--distributed_true', dest='distributed', action='store_true')
    parser.add_argument('--gpu_ids', nargs="+", default=['0', '1'])   # usage : --gpu_ids 0, 1, 2, 3
    parser.add_argument('--rank', type=int, default=0)
    parser.add_argument('--world_size', type=int)
    
    # data augmentation
    parser.add_argument('--mixup',  action='store_true', help='activate mixup augmentation')
    parser.add_argument('--alpha', default='1.0', type=float)

    return parser