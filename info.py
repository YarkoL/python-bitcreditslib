from bitcoin.core import b2lx
import bitcoin.wallet
import bitcoin.rpc

bitcoin.SelectParams('testnet')
rpc = bitcoin.rpc.Proxy()

print rpc.debug()

info = rpc.getinfo()
#print(b2lx(info))
print info
