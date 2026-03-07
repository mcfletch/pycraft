/**
 * Hook for inventory drag-and-drop state.
 *
 * Manages which slot is being dragged and which is highlighted as a drop
 * target. Shared across all grids in a single inventory view so items
 * can be dragged between sections (e.g. hotbar → armor, main → hotbar).
 *
 * Returns { dragOverSlot, handleDragStart, handleDragOver, handleDrop }
 */
import { useState, useRef } from 'react';

export function useInventoryDrag(onMove) {
  const [dragOverSlot, setDragOverSlot] = useState(null);
  const draggedSlot = useRef(null);

  const handleDragStart = (e, index) => {
    draggedSlot.current = index;
    e.dataTransfer.effectAllowed = 'move';
  };

  const handleDragOver = (e, index) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    setDragOverSlot(index);
  };

  const handleDrop = (e, index) => {
    e.preventDefault();
    setDragOverSlot(null);
    const from = draggedSlot.current;
    draggedSlot.current = null;
    if (from != null && from !== index && onMove) {
      onMove(from, index);
    }
  };

  return { dragOverSlot, handleDragStart, handleDragOver, handleDrop };
}
