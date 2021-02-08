#include<stdio.h>
#include<string.h>

int main() {
        setvbuf(stdout, NULL, _IONBF, 0);
			  //"something"
        char password[] = "R3k##!js@";

        char buf[256];

        printf("Gets 9 byte password in 256 byte buffer:\n");

        gets(buf);

        //printf("pas: %s\n", password);
        //printf("buf: %s\n", buf);
        printf("Strcmparing password...\n");
        int res = strcmp(password, buf);

        //printf("%d", res);

        if (res == 0) {
                printf("Welcome Dracula\n"); 
                printf("[ 1.6767021 Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)\n" \
                        "[ 1.077718] CPU: O PID: 1 COMM: Swapper/0 Not tainted 3.10.0-327.el7.x86_64 #1\n" \
                        "[ 1.078657) Hardware name: VMware, Inc. VMware Virtual Platform/440BX Desktop Reference Platform, BIOS 6.00 07/31/2013\n" \
                        "[ 1.081446) ffff88013938790 000000001e6559f5 000000001e6559f5 ffff880139387eo\n"\
                        "[ 1.082371] Call Trace:\n"\
                        "[ 1.082616] [<ffffffff816351f1>] dump_stack+8x19/0x1b\n" \
                        "[ 1.083005] [<ffffffff8162ea6c>] panic Bxd8/0x1e7\n"\
                        "[ 1.083382] [<ffffffff81a8d5fa>] Mount_block_root+0x2a1/0x2b0\n" \
                        "[ 1.083826) [<ffffffff81a8d65c>] Mount_root+0x53/0x56\n" \
                        "[ 1.084223] [<ffffffff81a8d79b>] prepare_namespace+0x13c/0x174\n" \
                        "[ 1.082616] [<ffffffff8163a3a1>] magpie{d()nt_p@n!k_pIz}\n" \
                        "[ 1.884667) [<ffffffff81a8d268>] kernel_init_freeable+8x1f0/0x217\n" \
                        "[ 1.085125] [<ffffffff81a8c9db>] ? initcall_blacklist +0xb0/0xb0\n" \
                        "[ 1.885570) [<ffffffff81624e10>] ? rest_init+0x80/0x80\n" \
                        "[ 1.085961] [<ffffffff81624e1e>] kernel_init+0xe/Oxfo\n" \
                        "[ 1.087300) [<ffffffff81645858>] ret_from_fork+x58/8x90\n" \
                        "[ 1.988660] [<ffffffff81624e10>] ? rest_init+0x80/0x80\n");
        }
        else { printf("Wrong password\n"); }
        return 1;
}

