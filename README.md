�R�}���h������s�}�N��  �wmultiExec_from_Python3 on Windows�x  
==
Windows�ł�Python3����R�}���h���}���`�v���Z�X�ŕ�����s����T���v���v���O�����ł��B   
  

## �V�X�e���v��
*Windows XP/Vista/7/8/10 or Windows Server 2008/2012/2016  
*Python 3.6�ȍ~

## �_�E�����[�h����ю��s���@

�R�}���h �v�����v�g�i�܂���PowerShell�j���J���Agit �Ń_�E�����[�h���܂��B  
```
>git clone https://github.com/gx3n-inue/multiExec_from_Python3
```

## ���s���@
  
1.�C�ӂ̃e�L�X�g�t�@�C��(cmdList.txt)�Ɏ��s�������R�}���h���񋓂��Ă����܂��B�P�s�P�R�}���h�ŋL�����Ă��������B

2.���L�̏�����Python�X�N���v�g�����s���܂��B
```
>python multiExec.py cmdListFileName <maxProcessCount> <interval> <retryCount> <waitExit>
```
  
���s��P�i�ő�v���Z�X�� = 4, �v���Z�X�ꗗ�擾�Ԋu = 4[s], �v���Z�X�ꗗ�Ď擾��  = 4, �N�������v���Z�X�̏I����҂��Ȃ��j  
```
>python multiExec.py cmdList.txt
```

���s��Q�i�ő�v���Z�X�� = 4, �v���Z�X�ꗗ�擾�Ԋu = 4[s], �v���Z�X�ꗗ�Ď擾��  = 4, �N�������v���Z�X�̏I����҂j  
>python multiExec.py cmdList.txt 4 4 4 1


## ���C�Z���X
  
�R�}���h������s�}�N���wmultiExec_from_Python3�x ver1.00  
This project is licensed under the terms of the MIT license, see LICENSE.  
