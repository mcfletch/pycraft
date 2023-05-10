.. currentmodule:: pycraft.server.final

ConsoleCommandSender
====================

Inheritance
------------
* pycraft.server.final.ConsoleCommandSender
* :py:class:`pycraft.server.final.CommandSender`
* :py:class:`pycraft.server.final.Permissible`
* :py:class:`pycraft.server.final.ServerOperator`
* :py:class:`pycraft.server.final.Conversable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.command.ConsoleCommandSender <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/command/ConsoleCommandSender.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ConsoleCommandSender(self, **named)
   :canonical: pycraft.server.final.ConsoleCommandSender

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: abandonConversation

       .. py:method:: abandonConversation(self, _0:Conversation) -> None
          :async:
          :noindex:

       .. py:method:: abandonConversation(self, _0:Conversation, _1:ConversationAbandonedEvent) -> None
          :async:
          :noindex:


   .. py:method:: acceptConversationInput(self, _0:String) -> None
      :async:


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


   .. py:method:: beginConversation(self, _0:Conversation) -> bool
      :async:


   .. py:method:: clearTitle(self) -> None
      :async:


   .. py:method:: deleteMessage

       .. py:method:: deleteMessage(self, _0:Signature) -> None
          :async:
          :noindex:

       .. py:method:: deleteMessage(self, _0:SignedMessage) -> None
          :async:
          :noindex:


   .. py:method:: filterAudience(self, _0:Predicate) -> :py:class:`Audience`
      :async:


   .. py:method:: forEachAudience(self, _0:Consumer) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: get(self, _0:Pointer) -> :py:class:`Optional`
      :async:


   .. py:method:: getEffectivePermissions(self) -> typing.List[:py:class:`PermissionAttachmentInfo`]
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getOrDefault(self, _0:Pointer, _1:Object) -> :py:class:`Object`
      :async:


   .. py:method:: getOrDefaultFrom(self, _0:Pointer, _1:Supplier) -> :py:class:`Object`
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


   .. py:method:: hideBossBar(self, _0:BossBar) -> None
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isConversing(self) -> bool
      :async:


   .. py:method:: isOp(self) -> bool
      :async:


   .. py:method:: isPermissionSet

       .. py:method:: isPermissionSet(self, _0:String) -> bool
          :async:
          :noindex:

       .. py:method:: isPermissionSet(self, _0:Permission) -> bool
          :async:
          :noindex:


   .. py:method:: name(self) -> :py:class:`Component`
      :async:


   .. py:method:: openBook

       .. py:method:: openBook(self, _0:Book) -> None
          :async:
          :noindex:

       .. py:method:: openBook(self, _0:Builder) -> None
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

       .. py:method:: playSound(self, _0:Sound) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Sound, _1:Emitter) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Sound, _1:double, _2:double, _3:double) -> None
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

       .. py:method:: sendActionBar(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendActionBar(self, _0:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendMessage

       .. py:method:: sendMessage(self, _0:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:BaseComponent) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:String[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:String) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:UUID, _1:String) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:UUID, _1:String[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identity, _1:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:SignedMessage, _1:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:ComponentLike, _1:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Component, _1:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Component, _1:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:ComponentLike, _1:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identified, _1:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identity, _1:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identified, _1:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identity, _1:Component, _2:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identified, _1:Component, _2:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identity, _1:ComponentLike, _2:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identified, _1:ComponentLike, _2:MessageType) -> None
          :async:
          :noindex:


   .. py:method:: sendPlainMessage(self, _0:String) -> None
      :async:


   .. py:method:: sendPlayerListFooter

       .. py:method:: sendPlayerListFooter(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendPlayerListFooter(self, _0:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendPlayerListHeader

       .. py:method:: sendPlayerListHeader(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendPlayerListHeader(self, _0:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendPlayerListHeaderAndFooter

       .. py:method:: sendPlayerListHeaderAndFooter(self, _0:Component, _1:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendPlayerListHeaderAndFooter(self, _0:ComponentLike, _1:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendRawMessage

       .. py:method:: sendRawMessage(self, _0:String) -> None
          :async:
          :noindex:

       .. py:method:: sendRawMessage(self, _0:UUID, _1:String) -> None
          :async:
          :noindex:


   .. py:method:: sendRichMessage(self, _0:String) -> None
      :async:


   .. py:method:: sendTitlePart(self, _0:TitlePart, _1:Object) -> None
      :async:


   .. py:method:: setOp(self, _0:boolean) -> None
      :async:


   .. py:method:: showBossBar(self, _0:BossBar) -> None
      :async:


   .. py:method:: showTitle(self, _0:Title) -> None
      :async:


   .. py:method:: stopSound

       .. py:method:: stopSound(self, _0:SoundStop) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, _0:Sound) -> None
          :async:
          :noindex:

