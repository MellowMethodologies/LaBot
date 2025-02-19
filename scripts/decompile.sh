#!/bin/sh

export DofusInvoker="/home/fake/.config/Ankama/Dofus/DofusInvoker.swf"
export selectclass='com.ankamagames.dofus.BuildInfos,com.ankamagames.dofus.network.++,com.ankamagames.jerakine.network.++'
export config='parallelSpeedUp=0'

cd "$( dirname "${BASH_SOURCE[0]}" )"
cd ..

rm -r sources

/home/fake/jpexs-decompiler/resources/ffdec.sh \
  -config "$config" \
    -selectclass "$selectclass" \
      -export script \
        ./sources $DofusInvoker
