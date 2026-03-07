import { useMutation, useQueryClient } from '@tanstack/react-query';
import { fetchApi } from './client';

export function useTeleportPlayer() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ uuid, world, x, y, z }) =>
      fetchApi(`/players/${uuid}/teleport`, {
        method: 'POST',
        body: JSON.stringify({ world, x, y, z }),
      }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['players'] });
    },
  });
}

export function useGiveItem() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ uuid, material, count, enchant, enchantments, potion_type, potion_effects, potion_name }) =>
      fetchApi(`/players/${uuid}/inventory/give`, {
        method: 'POST',
        body: JSON.stringify({ material, count, enchant: !!enchant, enchantments, potion_type, potion_effects, potion_name }),
      }),
    onSuccess: (_, variables) => {
      queryClient.invalidateQueries({ queryKey: ['players', variables.uuid, 'inventory'] });
    },
  });
}

export function useEnchantItem() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ uuid, slot, enchantments, potion_type, potion_effects, potion_name }) =>
      fetchApi(`/players/${uuid}/inventory/enchant`, {
        method: 'POST',
        body: JSON.stringify({ slot, enchantments, potion_type, potion_effects, potion_name }),
      }),
    onSuccess: (_, variables) => {
      queryClient.invalidateQueries({ queryKey: ['players', variables.uuid, 'inventory'] });
    },
  });
}

export function useDropItem() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ uuid, slot }) =>
      fetchApi(`/players/${uuid}/inventory/drop`, {
        method: 'POST',
        body: JSON.stringify({ slot }),
      }),
    onSuccess: (_, variables) => {
      queryClient.invalidateQueries({ queryKey: ['players', variables.uuid, 'inventory'] });
    },
  });
}

export function useMoveItem() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ uuid, from_slot, to_slot }) =>
      fetchApi(`/players/${uuid}/inventory/move`, {
        method: 'POST',
        body: JSON.stringify({ from_slot, to_slot }),
      }),
    onSuccess: (_, variables) => {
      queryClient.invalidateQueries({ queryKey: ['players', variables.uuid, 'inventory'] });
    },
  });
}

export function useSpawnEntity() {
  return useMutation({
    mutationFn: ({ worldName, type, x, y, z }) =>
      fetchApi(`/worlds/${worldName}/entities/spawn`, {
        method: 'POST',
        body: JSON.stringify({ type, x, y, z }),
      }),
  });
}

export function useSetBlocks() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ worldName, locations, material }) =>
      fetchApi(`/worlds/${worldName}/blocks`, {
        method: 'POST',
        body: JSON.stringify({ locations, material }),
      }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['worlds'] });
    },
  });
}

export function usePasteTemplate() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ worldName, template_name, x, y, z, rotation }) =>
      fetchApi(`/worlds/${worldName}/paste`, {
        method: 'POST',
        body: JSON.stringify({ template_name, x, y, z, rotation }),
      }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['worlds'] });
    },
  });
}

export function useEvalCode() {
  return useMutation({
    mutationFn: ({ code, player_uuid, map_context }) =>
      fetchApi('/eval', {
        method: 'POST',
        body: JSON.stringify({ code, player_uuid, map_context }),
      }),
  });
}
