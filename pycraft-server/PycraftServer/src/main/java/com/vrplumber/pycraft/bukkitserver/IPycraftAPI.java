package com.vrplumber.pycraft.bukkitserver;

public interface IPycraftAPI {
  public void setWanted(boolean wanted);

  public PycraftServerPlugin getPlugin();

  public boolean send(String formatted);

  public String sendResponse(Integer request, String formatted);

  public void dispatch(String line, boolean async);
}