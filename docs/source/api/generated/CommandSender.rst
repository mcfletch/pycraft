.. currentmodule:: pycraft.server.final

CommandSender
=============

Inheritance
------------
* pycraft.server.final.CommandSender
* :py:class:`pycraft.server.final.Permissible`
* :py:class:`pycraft.server.final.ServerOperator`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.command.CommandSender <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/command/CommandSender.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: CommandSender(self, **named)
   :canonical: pycraft.server.final.CommandSender

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addAttachment

       .. py:method:: addAttachment(self, _0:Plugin) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:

       .. py:method:: addAttachment(self, _0:Plugin, _1:int) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:

       .. py:method:: addAttachment(self, _0:Plugin, _1:String, _2:boolean) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:

       .. py:method:: addAttachment(self, _0:Plugin, _1:String, _2:boolean, _3:int) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:


   .. py:method:: clearTitle(self) -> None
      :async:


   .. py:method:: deleteMessage

       .. py:method:: deleteMessage(self, signature:Signature) -> None
          :async:
          :noindex:

       .. py:method:: deleteMessage(self, signedMessage:SignedMessage) -> None
          :async:
          :noindex:


   .. py:method:: filterAudience(self, filter:Predicate) -> :py:class:`Audience`
      :async:


   .. py:method:: forEachAudience(self, action:Consumer) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: get(self, pointer:Pointer) -> :py:class:`Optional`
      :async:


   .. py:method:: getEffectivePermissions(self) -> typing.List[:py:class:`PermissionAttachmentInfo`]
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getOrDefault(self, pointer:Pointer, defaultValue:Object) -> :py:class:`Object`
      :async:


   .. py:method:: getOrDefaultFrom(self, pointer:Pointer, defaultValue:Supplier) -> :py:class:`Object`
      :async:


   .. py:method:: getServer(self) -> :py:class:`Server`
      :async:


   .. py:method:: hasPermission

       .. py:method:: hasPermission(self, _0:Permission) -> bool
          :async:
          :noindex:

       .. py:method:: hasPermission(self, _0:String) -> bool
          :async:
          :noindex:


   .. py:method:: hideBossBar(self, bar:BossBar) -> None
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isOp(self) -> bool
      :async:


   .. py:method:: isPermissionSet

       .. py:method:: isPermissionSet(self, _0:Permission) -> bool
          :async:
          :noindex:

       .. py:method:: isPermissionSet(self, _0:String) -> bool
          :async:
          :noindex:


   .. py:method:: name(self) -> :py:class:`Component`
      :async:


   .. py:method:: openBook

       .. py:method:: openBook(self, book:Book) -> None
          :async:
          :noindex:

       .. py:method:: openBook(self, book:Builder) -> None
          :async:
          :noindex:


   .. py:method:: permissionValue

       .. py:method:: permissionValue(self, _0:Permission) -> :py:class:`TriState`
          :async:
          :noindex:

       .. py:method:: permissionValue(self, _0:String) -> :py:class:`TriState`
          :async:
          :noindex:


   .. py:method:: playSound

       .. py:method:: playSound(self, sound:Sound) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, sound:Sound, emitter:Emitter) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, sound:Sound, x:double, y:double, z:double) -> None
          :async:
          :noindex:


   .. py:method:: pointers(self) -> :py:class:`Pointers`
      :async:


   .. py:method:: recalculatePermissions(self) -> None
      :async:


   .. py:method:: removeAttachment(self, _0:PermissionAttachment) -> None
      :async:


   .. py:method:: resetTitle(self) -> None
      :async:


   .. py:method:: sendActionBar

       .. py:method:: sendActionBar(self, message:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendActionBar(self, message:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendMessage

       .. py:method:: sendMessage(self, _0:BaseComponent) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, message:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, message:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:String) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:String[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, message:Component, boundChatType:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, message:Component, type:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, message:ComponentLike, boundChatType:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, message:ComponentLike, type:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, source:Identified, message:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, source:Identified, message:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, source:Identity, message:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, source:Identity, message:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, signedMessage:SignedMessage, boundChatType:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:UUID, _1:String) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:UUID, _1:String[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, source:Identified, message:Component, type:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, source:Identified, message:ComponentLike, type:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identity, _1:Component, _2:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, source:Identity, message:ComponentLike, type:MessageType) -> None
          :async:
          :noindex:


   .. py:method:: sendPlainMessage(self, _0:String) -> None
      :async:


   .. py:method:: sendPlayerListFooter

       .. py:method:: sendPlayerListFooter(self, footer:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendPlayerListFooter(self, footer:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendPlayerListHeader

       .. py:method:: sendPlayerListHeader(self, header:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendPlayerListHeader(self, header:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendPlayerListHeaderAndFooter

       .. py:method:: sendPlayerListHeaderAndFooter(self, header:Component, footer:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendPlayerListHeaderAndFooter(self, header:ComponentLike, footer:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendRichMessage(self, _0:String) -> None
      :async:


   .. py:method:: sendTitlePart(self, part:TitlePart, value:Object) -> None
      :async:


   .. py:method:: setOp(self, _0:boolean) -> None
      :async:


   .. py:method:: showBossBar(self, bar:BossBar) -> None
      :async:


   .. py:method:: showTitle(self, title:Title) -> None
      :async:


   .. py:method:: stopSound

       .. py:method:: stopSound(self, sound:Sound) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, stop:SoundStop) -> None
          :async:
          :noindex:

