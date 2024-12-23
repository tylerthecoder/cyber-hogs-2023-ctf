#include <stdint.h>
#include <stdio.h>
#include <string.h>

int main(long param_2) {
  long lVar1;
  int iVar2;
  size_t sVar3;
  long in_FS_OFFSET;
  int local_50;
  int local_4c;
  int local_48;
  byte local_38[30];
  undefined local_1a;
  long local_10;

  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  if (param_1 < 2) {
    puts("You need to give me an argument to check the flag!");
  } else {
    sVar3 = strlen(*(char **)(param_2 + 8));
    if ((int)sVar3 == 0x1e) {
      lVar1 = *(long *)(param_2 + 8);
      for (local_50 = 0; local_50 < 0x1e; local_50 = local_50 + 1) {
        local_38[local_50] = *(byte *)(lVar1 + local_50);
      }
      local_1a = 0;
      for (local_4c = 0; local_4c < 0x1e; local_4c = local_4c + 1) {
        local_38[local_4c] = local_38[local_4c] ^ "fried"[local_4c % 5];
      }
      for (local_48 = 0; local_48 < 0x1e; local_48 = local_48 + 1) {
        local_38[local_48] = local_38[local_48] ^ "chickens"[local_48 % 8];
      }
      iVar2 = strcmp((char *)local_38, "cvaatd}v`Sjyv_npbsiqheXsqosUg|");
      if (iVar2 == 0) {
        puts("Success, flag is correct!");
      } else {
        puts("Wrong answer!");
      }
    } else {
      puts("Wrong size!");
    }
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
