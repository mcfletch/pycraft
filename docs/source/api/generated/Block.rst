.. currentmodule:: pycraft.server.final

Block
=====

Inheritance
------------
* pycraft.server.final.Block
* :py:class:`pycraft.server.world.Block`
* :py:class:`pycraft.server.final.Metadatable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.block.Block <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Block.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Block(self, **named)
   :canonical: pycraft.server.final.Block

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: applyBoneMeal(self, _0:BlockFace) -> bool
      :async:


   .. py:method:: breakNaturally

       .. py:method:: breakNaturally(self) -> bool
          :async:
          :noindex:

       .. py:method:: breakNaturally(self, _0:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: breakNaturally(self, _0:ItemStack) -> bool
          :async:
          :noindex:

       .. py:method:: breakNaturally(self, _0:boolean, _1:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: breakNaturally(self, _0:ItemStack, _1:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: breakNaturally(self, _0:ItemStack, _1:boolean, _2:boolean) -> bool
          :async:
          :noindex:


   .. py:method:: canPlace(self, _0:BlockData) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBiome(self) -> :py:class:`Biome`
      :async:


   .. py:method:: getBlockData(self) -> :py:class:`BlockData`
      :async:


   .. py:method:: getBlockKey

       .. py:method:: getBlockKey(self) -> :py:class:`long`
          :async:
          :noindex:

       .. py:method:: getBlockKey(cls, _0:int, _1:int, _2:int) -> :py:class:`long`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: getBlockKeyX(cls, _0:long) -> int
      :async:
      :classmethod:


   .. py:method:: getBlockKeyY(cls, _0:long) -> int
      :async:
      :classmethod:


   .. py:method:: getBlockKeyZ(cls, _0:long) -> int
      :async:
      :classmethod:


   .. py:method:: getBlockPower

       .. py:method:: getBlockPower(self) -> int
          :async:
          :noindex:

       .. py:method:: getBlockPower(self, _0:BlockFace) -> int
          :async:
          :noindex:


   .. py:method:: getBlockSoundGroup(self) -> :py:class:`SoundGroup`
      :async:


   .. py:method:: getBoundingBox(self) -> :py:class:`BoundingBox`
      :async:


   .. py:method:: getBreakSpeed(self, _0:Player) -> float
      :async:


   .. py:method:: getChunk(self) -> :py:class:`Chunk`
      :async:


   .. py:method:: getCollisionShape(self) -> :py:class:`VoxelShape`
      :async:


   .. py:method:: getComputedBiome(self) -> :py:class:`Biome`
      :async:


   .. py:method:: getData(self) -> :py:class:`byte`
      :async:


   .. py:method:: getDestroySpeed

       .. py:method:: getDestroySpeed(self, _0:ItemStack) -> float
          :async:
          :noindex:

       .. py:method:: getDestroySpeed(self, _0:ItemStack, _1:boolean) -> float
          :async:
          :noindex:


   .. py:method:: getDrops

       .. py:method:: getDrops(self) -> typing.List[:py:class:`ItemStack`]
          :async:
          :noindex:

       .. py:method:: getDrops(self, _0:ItemStack) -> typing.List[:py:class:`ItemStack`]
          :async:
          :noindex:

       .. py:method:: getDrops(self, _0:ItemStack, _1:Entity) -> typing.List[:py:class:`ItemStack`]
          :async:
          :noindex:


   .. py:method:: getFace(self, _0:Block) -> :py:class:`BlockFace`
      :async:


   .. py:method:: getHumidity(self) -> float
      :async:


   .. py:method:: getLightFromBlocks(self) -> :py:class:`byte`
      :async:


   .. py:method:: getLightFromSky(self) -> :py:class:`byte`
      :async:


   .. py:method:: getLightLevel(self) -> :py:class:`byte`
      :async:


   .. py:method:: getLocation

       .. py:method:: getLocation(self) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: getLocation(self, _0:Location) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: getMetadata(self, _0:String) -> typing.List[:py:class:`MetadataValue`]
      :async:


   .. py:method:: getPistonMoveReaction(self) -> :py:class:`PistonMoveReaction`
      :async:


   .. py:method:: getRelative

       .. py:method:: getRelative(self, _0:BlockFace) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getRelative(self, _0:BlockFace, _1:int) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getRelative(self, _0:int, _1:int, _2:int) -> :py:class:`Block`
          :async:
          :noindex:


   .. py:method:: getSoundGroup(self) -> :py:class:`BlockSoundGroup`
      :async:


   .. py:method:: getState

       .. py:method:: getState(self) -> :py:class:`BlockState`
          :async:
          :noindex:

       .. py:method:: getState(self, _0:boolean) -> :py:class:`BlockState`
          :async:
          :noindex:


   .. py:method:: getTemperature(self) -> float
      :async:


   .. py:method:: getTranslationKey(self) -> str
      :async:


   .. py:method:: getType(self) -> :py:class:`Material`
      :async:


   .. py:method:: getWorld(self) -> :py:class:`World`
      :async:


   .. py:method:: getX(self) -> int
      :async:


   .. py:method:: getY(self) -> int
      :async:


   .. py:method:: getZ(self) -> int
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hasMetadata(self, _0:String) -> bool
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isBlockFaceIndirectlyPowered(self, _0:BlockFace) -> bool
      :async:


   .. py:method:: isBlockFacePowered(self, _0:BlockFace) -> bool
      :async:


   .. py:method:: isBlockIndirectlyPowered(self) -> bool
      :async:


   .. py:method:: isBlockPowered(self) -> bool
      :async:


   .. py:method:: isBuildable(self) -> bool
      :async:


   .. py:method:: isBurnable(self) -> bool
      :async:


   .. py:method:: isCollidable(self) -> bool
      :async:


   .. py:method:: isEmpty(self) -> bool
      :async:


   .. py:method:: isLiquid(self) -> bool
      :async:


   .. py:method:: isPassable(self) -> bool
      :async:


   .. py:method:: isPreferredTool(self, _0:ItemStack) -> bool
      :async:


   .. py:method:: isReplaceable(self) -> bool
      :async:


   .. py:method:: isSolid(self) -> bool
      :async:


   .. py:method:: isValidTool(self, _0:ItemStack) -> bool
      :async:


   .. py:method:: randomTick(self) -> None
      :async:


   .. py:method:: rayTrace(self, _0:Location, _1:Vector, _2:double, _3:FluidCollisionMode) -> :py:class:`RayTraceResult`
      :async:


   .. py:method:: removeMetadata(self, _0:String, _1:Plugin) -> None
      :async:


   .. py:method:: setBiome(self, _0:Biome) -> None
      :async:


   .. py:method:: setBlockData

       .. py:method:: setBlockData(self, _0:BlockData) -> None
          :async:
          :noindex:

       .. py:method:: setBlockData(self, _0:BlockData, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setMetadata(self, _0:String, _1:MetadataValue) -> None
      :async:


   .. py:method:: setType

       .. py:method:: setType(self, _0:Material) -> None
          :async:
          :noindex:

       .. py:method:: setType(self, _0:Material, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: tick(self) -> None
      :async:


   .. py:method:: translationKey(self) -> str
      :async:

