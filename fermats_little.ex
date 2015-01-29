defmodule Fermat do
  def base do 7 end
  def gen(f, a, b) do rem(f.(a, b), base) end
  def sum(a, b) do gen(&(&1+&2), a, b) end
  def minus(a, b) do gen(&(&1-&2), a, b) end
  def times(a, b) do gen(&(&1*&2), a, b) end
  def divide(a, b) do gen(&(div(&1,&2)), a, b) end
  def power(a, b) do
    cond do
      a==0 -> 0
      a==1 -> 1
      b==0 -> 1
      b==1 -> a
      rem(b, 2)==0 -> power(a*a, div(b,2))
      true -> a*power(a, b-1)
    end
  end
  def test do
    f= fn(x) -> rem(power(x, 12), 13) |> inspect |> IO.puts end
    Enum.map(0..7, f)
  end
end
