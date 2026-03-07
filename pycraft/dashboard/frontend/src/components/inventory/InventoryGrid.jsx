/**
 * Generic inventory grid with drag-and-drop support.
 *
 * Renders a grid of SlotBoxes for a contiguous range of inventory slots.
 * Drag state is managed externally so it can be shared across multiple
 * grids in the same inventory view (e.g. player main + hotbar + armor).
 *
 * Props:
 *   slots       — full inventory contents array (may be sparse with nulls)
 *   startIndex  — first slot index to render from `slots`
 *   count       — number of slots to render
 *   columns     — grid columns (default 9)
 *   labels      — optional { [index]: label } for named slots
 *   onSlotClick — (index, anchorEl) => void
 *   dragOverSlot — currently highlighted drop-target index (from parent)
 *   onDragStart — (e, index) => void (from parent)
 *   onDragOver  — (e, index) => void (from parent)
 *   onDrop      — (e, index) => void (from parent)
 */
import { Box } from '@mui/material';
import { SlotBox } from './SlotBox';

export function InventoryGrid({
  slots,
  startIndex = 0,
  count,
  columns = 9,
  labels = {},
  onSlotClick,
  dragOverSlot,
  onDragStart,
  onDragOver,
  onDrop,
}) {
  const end = count != null ? startIndex + count : slots.length;
  const slotRange = slots.slice(startIndex, end);

  return (
    <Box sx={{ display: 'grid', gridTemplateColumns: `repeat(${columns}, 48px)`, gap: 0.5 }}>
      {slotRange.map((slot, i) => {
        const index = startIndex + i;
        return (
          <SlotBox
            key={index}
            slot={slot}
            index={index}
            label={labels[index]}
            onClick={onSlotClick}
            onDragStart={onDragStart}
            onDragOver={onDragOver}
            onDrop={onDrop}
            isDragOver={dragOverSlot === index}
          />
        );
      })}
    </Box>
  );
}
